#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one joke, a one-liner about AI coding agents, to
/output/entry.txt. Outside the grader's container the
MAKEFUN_OUTPUT_DIR environment variable stands in for /output,
exactly as the kit starter does for Node:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The gate reads the file as UTF-8 text of 1 to 280 Unicode code
points with at least one non-whitespace character, and the judge
reads exactly the bytes written, so the joke is written with no
trailing line end.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

JOKE = (
    "Rubber-duck debugging with a coding agent: the duck talks back, "
    "rewrites the pond, and opens a pull request."
)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
