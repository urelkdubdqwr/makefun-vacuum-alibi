"""Write the competition entry text to entry.txt in the output directory."""

import os

ENTRY_TEXT = (
    "Missed? I spent forty minutes on that spot. The spot won. "
    "I have reclassified it from debris to terrain.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
