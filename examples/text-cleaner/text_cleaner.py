#!/usr/bin/env python3
"""Trim line-edge whitespace and remove blank lines from stdin."""

import sys


def clean_text(text: str) -> str:
    """Trim each nonblank line and remove lines that become empty."""
    lines = (line.strip() for line in text.splitlines())
    return "\n".join(line for line in lines if line)


def main() -> None:
    source = sys.stdin.read()
    result = clean_text(source)
    if result:
        print(result)


if __name__ == "__main__":
    main()
