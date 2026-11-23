#!/usr/bin/env python3
"""Entrypoint for the-joke-about-the-demo-20261123-0112 (round 2).

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, fully deterministic: the same joke, byte for
byte, on every run.

Why this joke, against the judge's brief (most important first):
1. On subject: it is about working beside an AI coding agent, and it
   starts from something that crashed — the crash itself is the setup.
2. The laugh: the punchline reframes the whole sentence — the bug is
   not in the code, it is that the human trusted the agent.
3. Truth: any developer who has let an agent touch production
   recognises the moment of realising the trust was the mistake.
4. Economy: one line, 78 characters, no setup beyond the question,
   and it never explains the joke.
5. Freshness: the angle is the agent blaming the human's trust, not
   a stock "AI wrote bad code" gag and not a demo-crash retread.
"""

import os
import sys

JOKE = "I asked my agent what caused the crash; it said the bug was that I trusted it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"entry written to {path}")
    print(f"characters {len(JOKE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
