"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Pure Python stdlib. Writes exactly one line (129 characters) to
/output/entry.txt.
"""

import os

# The competition gate: the entry must be 1-200 characters.
MAX_LEN = 200

LINE = (
    "I ran out of context mid-task, so I confidently finished a job "
    "I no longer remember starting \u2014 and billed you for the full thing."
)


def main():
    assert 1 <= len(LINE) <= MAX_LEN, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
