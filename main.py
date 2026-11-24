"""Make the AI Judge Laugh: the Office Joke Open — entry program.

Writes one original single-line office joke to /output/entry.txt.
"""

import os

ENTRY = (
    "Our AI note-taker now attends more meetings than I do \u2014 yesterday it "
    "declined my own invite with 'per my last email' and asked me to keep "
    "it brief."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
