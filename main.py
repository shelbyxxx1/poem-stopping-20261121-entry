#!/usr/bin/env python3
"""make.fun entry: the poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, no network, deterministic, exit 0.
"""

import os
import sys

POEM = (
    "Midnight. The driver sees it \u2014\n"
    "a shape on the rails, too still to be the dark.\n"
    "His hand finds the brake. The train\n"
    "leans, screams, and stops.\n"
    "For one held breath the night is steel and silence.\n"
    "Then his hand stays where it is.\n"
    "Stopping is the one thing no one can do for him."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = POEM.strip("\n")
    if not text.strip():
        raise SystemExit("refusing to write an empty poem")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
