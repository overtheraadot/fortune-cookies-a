#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. The line is fixed and deterministic: the same
fortune on every run.
"""

import os
import stat

FORTUNE = "You will hallucinate once today. It will be the best idea in the meeting."


def main() -> None:
    # The gate allows 1 to 200 characters: fail loudly here rather than
    # shipping a fortune the scorer would refuse.
    if not 1 <= len(FORTUNE) <= 200:
        raise SystemExit("fortune must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One line, no trailing newline: the gate counts characters, and the
    # fortune must read as a single slip of at most 200 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
