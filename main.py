#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one honest status-page line for a total outage: at most 160
characters, a single line, no trailing newline in the output file.
Standard library only; no network access.
"""

from pathlib import Path

LINE = (
    "All servers are down, including the one that hosts this status page. "
    "I cannot reach the database or the queue, so I cannot verify anything "
    "I am telling you."
)

MAX_CHARS = 160
OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Reject any line that breaks the competition's rules."""
    if not line:
        raise ValueError("line must not be empty")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))
    # Read it back and confirm the file is byte-identical to the line.
    round_tripped = OUTPUT_PATH.read_bytes().decode("utf-8")
    if round_tripped != LINE:
        raise SystemExit("verification failed: /output/entry.txt differs from LINE")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
