# Changelog

## 0.2.0

- Tunes lyrics-guided mode defaults: `--lyrics-min-score` now defaults to 0.50 and `--lyrics-target-coverage` defaults to 0.90.
- `--lyrics-target-coverage 0` disables the auto-relax behavior.
- Improves lyrics-mode logging: reports effective threshold and coverage.
- Exposes lyrics alignment stats on `GenerateResult` (`lyrics_effective_min_score`, `lyrics_target_coverage`, `lyrics_coverage`).

## 0.1.4

- Adds lyrics-guided generation: pass full lyrics and the generator will pick/cut each line from the canonical lyrics instead of relying on LLM correction.
- Adds CLI flags `--lyrics-file/--lyrics` (single-file mode).
- Adds GPU selection flags for transcription: `--device auto|cpu|cuda` and `--cuda-device`.

## 0.1.3

- Makes `openai` / OpenCC optional via extras: `lrcgen[online]`, `lrcgen[opencc]`, `lrcgen[full]`.
- Improves CLI validation: `--offline` and `--online` are now mutually exclusive.
- Fixes CI on Python 3.8/3.10 by using `tomli` fallback for reading `pyproject.toml`.

## 0.1.2

- Adds a stable library API (`lrcgen.api`) with sync wrappers.
- Supports `python -m lrcgen` module entrypoint and `--version/--model/--language` CLI flags.
- Improves LLM correction safety (strict line alignment + guardrails) and logging.
- Adds CI checks and a small unittest suite.
- Adds a cross-platform clean script (`tools/clean.py`) and documents a repeatable release flow.
- Switches GitHub Actions publishing to PyPI Trusted Publishing (OIDC) with attestations.

## 0.1.1

- Packaging/CI improvements and CLI enhancements.

## 0.1.0

- Initial release.
