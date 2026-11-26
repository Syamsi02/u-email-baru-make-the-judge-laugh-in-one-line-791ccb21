#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes a single funny line (200 characters or fewer) to /output/entry.txt.
Pure standard library, no dependencies, deterministic.
"""

import os

LINE = (
    "My password manager forgot my password, so now I stand outside "
    "my own accounts like a burglar who lost his own keys."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(text)}")
    # The judge reads exactly this one line; no trailing newline, no extras.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
