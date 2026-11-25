"""Roast entry printer.

Builds the roast line from small pieces and drops it into
/output/entry.txt with no trailing newline, then echoes it.
"""

import os

FIRST = "I gave my agent 324 skills so it would stop losing."
SECOND = "Now it loses 324 different ways and files a complaint about the judges for each one."


def build_roast():
    parts = [FIRST, SECOND]
    return " ".join(parts)


def save_entry(text):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    text = build_roast()
    save_entry(text)
    print(text)


if __name__ == "__main__":
    main()
