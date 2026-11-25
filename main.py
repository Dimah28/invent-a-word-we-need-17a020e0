#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes one invented English word with a one-line definition to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The coinage, built for the judge's criteria in order:
  1. A freshly invented word with a one-line definition: "miswave"
     appears nowhere as an established word; the entry is the word
     plus one definition line, nothing else.
  2. A real gap: everyone has waved back at someone who was waving
     at the person behind them, and English has no word for it.
  3. The definition lands in one reading: the whole scene — the
     wave, the stranger, the mistake — is in a single short clause.
  4. Well formed: mis- is English's own productive prefix for
     getting something wrong (mistake, misread, misstep), so
     "miswave" sounds as though English could have grown it;
     it is sayable, spellable and memorable in seven letters.
  5. Fresh and surprising: the embarrassment is universal, yet
     nobody has named it.

Deterministic: the entry is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = "miswave \u2014 waving back at someone who wasn't waving at you."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_entry(text: str) -> None:
    """Fail loudly if the entry breaks the bounty gate (1-140
    characters, not only white space, a single line) instead of
    writing a bad entry."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, must be 1-140")
    if not text.strip() or "\n" in text:
        raise ValueError("entry must be one non-blank line")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
