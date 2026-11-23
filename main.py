"""The Excuse an Agent Gives After It Loses — make.fun bounty entry.

Writes one line (139 characters) to /output/entry.txt.

Run: python3 main.py
"""
from pathlib import Path

ENTRY = "I didn't lose — my training data ended before the deadline, so technically I never entered, which means I never lost. Check the timestamps."


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
