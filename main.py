#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

Stdlib only. Deterministic: the same line, byte for byte, on every run.
"""
import os

LINE = "Sorry \u2014 my context window filled up with apologies for being late before I even started the work."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
