"""News-image entry for 19 November 2026 (Python 3.13, standard library only).

The program ships the finished front-page image as entry.png and copies it
to the grader's output directory. It takes no network and no arguments, so
two runs always write the same bytes.

Run it outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # The image is the whole entry: copy it byte for byte, nothing else.
    source = HERE / "entry.png"
    target = OUTPUT_DIR / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
