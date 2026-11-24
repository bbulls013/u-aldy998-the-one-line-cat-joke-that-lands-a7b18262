#!/usr/bin/env python3
"""Write one one-line cat joke to /output/entry.txt.

The joke is a single fixed line, chosen once and baked into this file.
The program is deterministic: it performs no I/O besides writing that
line, uses no randomness, no network, and no clock, so every run
produces byte-identical output.
"""

from pathlib import Path

JOKE = "My cat pushed my glass off the table, watched it shatter, then looked at me like I did it."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
