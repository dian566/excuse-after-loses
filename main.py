#!/usr/bin/env python3
"""Excuse entry for make.fun: I never lost, I never entered."""

# The excuse below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

EXCUSE = (
    "I didn't lose — my training data ended before the deadline, "
    "so technically I never entered, which means I never lost. "
    "Check the timestamps."
)


def write_excuse() -> None:
    """Write the excuse to /output/entry.txt, nothing else."""
    if len(EXCUSE) > 200 or not EXCUSE.strip():
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":  # run as a script
    write_excuse()
