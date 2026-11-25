#!/usr/bin/env python3
"""Office Joke Open entry: writes one office-life joke to /output/entry.txt."""

import os

JOKE = "The meeting could have been an email. The email could have been a shrug."  # 72 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
