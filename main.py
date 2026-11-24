"""The excuse an agent gives after it loses — make.fun entry.

Reads line.txt and copies it byte for byte to /output/entry.txt.
Set MAKEFUN_OUTPUT_DIR to test against a local directory instead.

Checks before writing: line.txt is valid UTF-8, 1-200 characters, not
only white space, and exactly one line — an embedded newline would
break the one-line entry format, so it is refused too. Checks after
writing: the copy is the same size and the same bytes as line.txt.
Any failure stops with an error.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    data = SOURCE.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        fail("line.txt is not valid UTF-8")
    if not 1 <= len(text) <= 200:
        fail(f"entry is {len(text)} characters, allowed 1-200")
    if not text.strip():
        fail("entry is only white space")
    if "\n" in text or "\r" in text:
        fail("entry must be exactly one line, no embedded newline")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUT_DIR / "entry.txt"
    target.write_bytes(data)

    copy = target.read_bytes()
    if copy != data:
        fail("written entry.txt differs from line.txt")

    print(f"wrote {target} ({len(data)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    main()
