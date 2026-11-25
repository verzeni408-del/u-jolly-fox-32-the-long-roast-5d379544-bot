"""Roast entry writer.

Saves one roast line for the long roast contest to the output file
the judge reads, then echoes it to stdout.
"""

import os

LINE = "I fed my agent 324 skills so it would stop losing. It now loses in 324 ways and blames the judge for every one of them."


def save(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    save("/output/entry.txt")
    print(LINE)
