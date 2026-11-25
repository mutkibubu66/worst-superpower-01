#!/usr/bin/env python3
"""Worst Superpower — make.fun one-line entry.

Writes the one-liner to /output/entry.txt with no trailing newline.
"""

import os

LINE = "My superpower is knowing exactly what to say - three hours after the conversation ends, in the shower, to absolutely no one."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
