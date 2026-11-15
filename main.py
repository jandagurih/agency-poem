"""Write a deterministic poem without using the network."""

import os
from pathlib import Path

POEM = """The Magnet

The magnet is round and the size of a doughnut.
It lives in the drawer with the good scissors.
When the family has said what it came to say
and the order is signed in two places,
you tape it over the device in his chest
and the thing that was going to save him
stops offering.

He asked for it plainly, the way a man
asks for water. I don't want to be brought back.
Then, after a while: stay.

What they don't tell you is the pace of it.
The heart, left alone, takes its time.
Half an hour. The room gets smaller.
The radiator ticks. Somebody's phone
buzzes once, in a coat, in the hall.

I keep my hand flat on the magnet.
It cannot slip. I know that. I stay anyway,
until his wife comes in and puts her hand
on mine, and we stand there together
holding a thing that is doing nothing,
waiting for him to finish."""

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
