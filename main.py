#!/usr/bin/env python3
"""make.fun entry for bounty news-image-20261120.

"Sum up 20 November's world news in one image."

The program copies the bundled entry.png — a one-page newspaper-style
world news atlas for Friday 20 November 2026, designed in Canva — to the
output directory. It is fully deterministic: no network access, no
randomness and no timestamps, so every run writes byte-identical output.

Output: <MAKEFUN_OUTPUT_DIR or /output>/entry.png
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
