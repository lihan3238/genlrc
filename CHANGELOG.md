# Changelog

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
