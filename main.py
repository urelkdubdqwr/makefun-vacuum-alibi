"""Write the competition entry text to entry.txt in the output directory.

The output directory is taken from MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise the literal directory /output. The directory is created if needed.
"""

import os
import sys

ENTRY_FILENAME = "entry.txt"
ENTRY_TEXT = (
    "Missed? I spent forty minutes on that spot. The spot won. "
    "I have reclassified it from debris to terrain.\n"
)


def output_directory() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    directory = output_directory()
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        sys.stderr.write(f"could not create output directory {directory!r}: {error}\n")
        raise SystemExit(1)
    with open(os.path.join(directory, ENTRY_FILENAME), "w", encoding="utf-8") as entry:
        entry.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
