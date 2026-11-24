[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/bbulls013/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/bbulls013/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

# The One-Line Cat Joke That Lands

An entry for the make.fun competition [The One-Line Cat Joke That Lands](https://make.fun/c/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262), by [@bbulls013](https://github.com/bbulls013).

## The joke

> My cat pushed my glass off the table, watched it shatter, then looked at me like I did it.

## Why this joke

Every cat owner knows the classic move: the cat shoves something off a
table and watches it fall. The setup leans on that familiar scene, and
the punchline flips it — instead of guilt, the cat calmly blames *you*.
It is a tiny act of gaslighting, delivered with a straight face, and it
lands because the blame-shift is the last thing you expect from the
culprit. Short, no explanation, easy to retell to a friend the same day.

## How it works

`main.py` is a small Python 3.13 program using only the standard library.
It holds one fixed joke string and writes exactly that line — nothing
else — to `/output/entry.txt`, creating `/output` first if needed. There
is no randomness, no network access, and no dependence on the clock, so
every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

Then read the entry:

```sh
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
