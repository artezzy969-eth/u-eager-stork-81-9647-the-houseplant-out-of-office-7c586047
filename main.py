"""The Houseplant Out-of-Office.

Writes a single out-of-office auto-reply, as sent by the office fern,
to entry.txt in the output directory.
"""

import os
from pathlib import Path

OUT_OF_OFFICE_REPLY = (
    "Out of office: I'm the fern. Unwatered since March, "
    "alive on spite and sunlight. Your email has been composted."
)

MAX_CHARS = 120


def build_reply() -> str:
    """Return the fern's auto-reply, enforcing the 1-120 char gate."""
    line = OUT_OF_OFFICE_REPLY.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"reply must be 1-{MAX_CHARS} chars, got {len(line)}")
    return line


def resolve_entry_path() -> Path:
    """Resolve entry.txt under MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    resolve_entry_path().write_text(build_reply() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
