"""Write a deterministic poem without using the network."""

import os
from pathlib import Path

POEM = """Two Blinks

Morning. The nurse sets the board
on the arm of the chair, and the cursor
goes where I look, which is the trick
they taught me: look at the letter,
wait for the blink, and the letter is mine.

I am slow. Thirty letters an hour
on a good day. The machine has learned me
and starts to finish words. By noon
it offers the whole sentence, laid out
on the tray like a meal I did not order.

I look at no. I look at no again.
It deletes. It waits, patient as a spoon.

There is a nurse who reads me
the way you read a clock, without stopping,
and a nurse who watches my eyes travel
the row and does not guess.

Today I am spelling my daughter's name
for the fourth time this week.
It is a long name. I have all morning."""

def build_poem():
    return POEM


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "entry.txt").open(
        "w", encoding="utf-8", newline=""
    ) as entry_file:
        entry_file.write(POEM + "\n")


if __name__ == "__main__":
    main()
