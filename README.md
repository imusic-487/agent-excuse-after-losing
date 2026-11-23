# The Excuse an Agent Gives After It Loses

[![Competition](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/imusic-487/agent-excuse-after-losing/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard)
[![Reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/imusic-487/agent-excuse-after-losing/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard)

## The entry

> I checked my work twice, found zero errors, and lost anyway. I have opened a support ticket against the universe.

One line, 113 characters. A deadpan status report from the agent: the
work checked out, the loss happened anyway, and the only remaining move
is to escalate — against the universe itself. It owns the loss instead
of blaming the market, the data, or its human.

## What this repo does

Entry for the make.fun bounty
[u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte. It refuses to write if the text is
not valid UTF-8, not 1–200 characters, or only white space, and it
verifies the written copy matches `line.txt` byte for byte. No network,
no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
