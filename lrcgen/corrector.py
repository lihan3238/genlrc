from __future__ import annotations

import re
import asyncio
import sys
from openai import OpenAI
from .config import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL,
    OPENAI_MODEL,
    MAX_LLM_CONCURRENCY,
)

# ===== OpenAI Client =====
client = None
if OPENAI_API_KEY:
    client = OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )

_semaphore = asyncio.Semaphore(MAX_LLM_CONCURRENCY)


def needs_llm_fix(lines: list[str]) -> bool:
    """
    判断是否值得花钱纠错
    """
    if len(lines) < 8:
        return False

    total = len(lines)
    short = sum(1 for l in lines if len(l) <= 2)
    trad = sum(1 for l in lines if re.search(r"[裏爲妳祢著]", l))

    if short / total > 0.3:
        return True
    if trad / total > 0.2:
        return True

    return False


async def llm_fix(lines: list[str]) -> list[str]:
    """
    二次纠正（失败自动回退）
    """
    if not client:
        print(
            "[lrcgen] LLM correction skipped: OPENAI_API_KEY not set.",
            file=sys.stderr,
        )
        return lines

    async with _semaphore:
        try:
            joined = "\n".join(lines)
            prompt = f"""
以下是自动语音识别得到的中文歌词，请严格遵守：

1. 只纠正明显错别字、同音字
2. 不改变顺序
3. 不增加或删除任何一行
4. 行数必须完全一致
5. 只输出歌词正文

歌词如下：
{joined}
"""

            resp = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )

            fixed = resp.choices[0].message.content.strip().splitlines()
            if len(fixed) != len(lines):
                print(
                    f"[lrcgen] LLM correction ignored: line count mismatch ({len(fixed)} != {len(lines)})",
                    file=sys.stderr,
                )
                return lines
            return fixed

        except Exception as e:
            print(f"[lrcgen] LLM correction failed: {e}", file=sys.stderr)
            return lines
