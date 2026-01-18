from __future__ import annotations

import glob
import shutil
from pathlib import Path


def _rm(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    # Common build artifacts
    targets = [
        root / "dist",
        root / "build",
        root / ".pytest_cache",
        root / ".mypy_cache",
        root / ".ruff_cache",
    ]

    # egg-info folders (glob)
    for p in glob.glob(str(root / "*.egg-info")):
        targets.append(Path(p))

    removed = 0
    for t in targets:
        if t.exists():
            _rm(t)
            removed += 1

    print(f"clean: removed {removed} artifact(s)")


if __name__ == "__main__":
    main()
