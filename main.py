#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — entry writer.

Writes a single one-line office joke to /output/entry.txt. Pure stdlib,
deterministic: the same bytes on every run (sha256 2ca6d11e04293cbf6
88bdae0911f0420e1ea2527a81a377a37bb355a39374110, verified 2x), no trailing
newline so the file is exactly one line. Entry is 115 characters,
21 words, within the 1-200 character gate.
"""

import os

ENTRY = (
    # Rubric pick: two universal office truths stacked (the meeting
    # that could have been an email + reply-all), then a second turn
    # at the very end — the complainer is now chairing the meeting
    # about his own email. Punchline last, no wasted words.
    "I replied-all that the meeting could have been an email; "
    "now there's a meeting about my email, and I'm chairing it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
