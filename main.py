"""The Long Roast — one line roasting my own AI agent.

Single line, no trailing newline: the joke is the whole entry.
"""

from pathlib import Path

ENTRY = "I asked my agent for one good idea. It spawned three subagents, held a meeting, and billed me for the brainstorm."


def main():
    Path("/output").mkdir(parents=True, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
