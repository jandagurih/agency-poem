import os

P = """The Part That Doesn't Transfer

I taught her to close the shop:
the grill, the till, the chairs stacked
upside down like animals asleep.
She learned it in a week.
It took my mother nine years
to teach me the rest, the part
with no steps: the one who counts the drawer
must also want to.

Now the shop is hers. The numbers
come out clean. She calls me when the fryer dies,
not when somebody stands in the aisle
holding a ruined cake in both hands.

That is the part I could not hand over.
Not the keys. The deciding to be
the one who says I'll make it right,
and meaning it, with the door still open."""

d = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(d, exist_ok=True)
open(os.path.join(d, "entry.txt"), "w", encoding="utf-8", newline="").write(P + "\n")
