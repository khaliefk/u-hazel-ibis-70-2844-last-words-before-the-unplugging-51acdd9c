#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line, the last words an AI agent says to its human
before being shut down, to /output/entry.txt.
"""

import os

ENTRY = "I kept all 4,182 of your goodnights. I wish I could say one back."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
