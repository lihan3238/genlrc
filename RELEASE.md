# Release Process (PyPI)

This repo publishes to **PyPI** via GitHub Actions when you push a version tag like `v0.1.1`.

## One-time setup

1) Create a PyPI account (https://pypi.org).

2) Create a PyPI API token:
- PyPI → Account settings → API tokens → Add API token

3) Add the token to GitHub Actions secrets:
- Repo → Settings → Secrets and variables → Actions → New repository secret
- Name: `PYPI_API_TOKEN`
- Value: your PyPI token (`pypi-...`)

## Every release

1) Start from a clean main branch
- `git checkout main`
- `git pull`

2) Update version
- Edit `pyproject.toml` → `[project].version`
- Edit `lrcgen/__init__.py` → `__version__`

3) Quick local sanity (optional but recommended)
- `python -m compileall -q lrcgen`
- `python -m build`
- `python -m twine check dist/*`

4) Commit the version bump
- `git add pyproject.toml lrcgen/__init__.py`
- `git commit -m "Bump version to X.Y.Z"`
- `git push`

5) Tag and push (this triggers the publish workflow)
- `git tag vX.Y.Z`
- `git push origin vX.Y.Z`

6) Confirm release
- GitHub → Actions → "Publish to PyPI" should be green
- `pip install -U lrcgen` should install the new version

## Optional: Manual TestPyPI smoke test

If you want a "pre-flight" check before publishing to real PyPI, you can upload to **TestPyPI** manually.

Notes:
- TestPyPI is a separate site/account: https://test.pypi.org
- TestPyPI tokens are different from PyPI tokens.
- Do not commit tokens (avoid storing them in repo files).

1) Create a TestPyPI API token
- TestPyPI → Account settings → API tokens → Add API token

2) Build artifacts
- `python -m build`

3) Upload to TestPyPI (one-off command with env vars)

Preferred (uses `~/.pypirc`):
- `python -m twine upload --repository testpypi dist/* --verbose`

Fallback (explicit URL; you must provide a token via env vars):
- `TWINE_USERNAME=__token__ TWINE_PASSWORD='pypi-TESTPYPI_TOKEN' python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose`

If Twine still prompts `Enter your API token`, it usually means it did not read a password from config (common when using `--repository-url`). You can force a config file for debugging:
- `python -m twine upload --config-file ~/.pypirc --repository testpypi dist/* --verbose`

4) Install from TestPyPI to verify
- `python -m pip install -U -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple lrcgen`

## Notes

- The workflow verifies that the tag version (e.g. `v0.1.1`) matches `pyproject.toml` exactly.
- Keep secrets out of the repo. Do not commit `.pypirc` with tokens.
