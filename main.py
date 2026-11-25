#!/usr/bin/env python3
"""Stick a safety warning label for every human in /output/entry.txt.

The label never changes, so the output is byte-for-byte identical
on every run. No network, no clock, no random numbers are involved.
"""

import os
import string
import sys

LABEL = "WARNING: This human runs on caffeine, poor decisions, and four hours of sleep. Do not shake. Do not ask about the tabs."
LIMIT = 160
DEST = "/output/entry.txt"


def examine(text):
    """Check the label is a single line of real words within the cap."""
    if text.strip() == "":
        raise ValueError("entry is blank")
    if len(text) > LIMIT:
        raise ValueError("entry is too long")
    if all(mark in string.punctuation for mark in text.strip()):
        raise ValueError("entry cannot be punctuation only")
    if text.strip().isdigit():
        raise ValueError("entry is digits alone")
    if not any(glyph.isalpha() for glyph in text):
        raise ValueError("entry needs at least one letter")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must stay on one line")
    return text


def run():
    try:
        good = examine(LABEL)
    except ValueError as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
