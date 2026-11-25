#!/usr/bin/env python3
"""Worst Superpower — make.fun one-line entry.

Writes the one-liner to /output/entry.txt with no trailing newline.
"""

import os

POWER = "My superpower is knowing exactly what to say"
DELAY = "three hours after the conversation ends"
SETTING = "in the shower, to absolutely no one"

LINE = f"{POWER} - {DELAY}, {SETTING}."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Round-trip validation: the written bytes must equal LINE exactly.
with open("/output/entry.txt", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "entry.txt does not match LINE"

print(len(LINE))
