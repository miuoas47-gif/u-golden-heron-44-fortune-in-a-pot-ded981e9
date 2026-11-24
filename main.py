#!/usr/bin/env python3
"""Fortune in a Pot — write one houseplant fortune to /output/entry.txt.

The fortune is a single line of at most 120 characters, written for the
plant on the windowsill: kind, a little funny, and shaped like a prediction.
The program is fully deterministic: the same run always writes the same
bytes, with no randomness, no network and no input.
"""

import os

FORTUNE = (
    "By spring, the sunbeam on your sill will pick your newest leaf first, "
    "and the other plants will call it favoritism."
)


def main() -> None:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"fortune is {len(text)} characters, must be 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
