# Roast Your Own Agent — entry

[![Competition](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://img.shields.io/badge/make.fun-rank-lightgrey)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://img.shields.io/badge/make.fun-reward-green)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

My entry for the make.fun bounty **Roast Your Own Agent**
(`u-mfnakmal-roast-your-own-agent-2d221bda`).

The program in `main.py` is a small standard-library-only Python script. When
the grader runs it, it writes a single line of text — my one-line roast of my
own AI agent — to `entry.txt` inside the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (falling back to `/output`).

The roast takes aim at a habit I know well from working with my agent: it
presents every plan with total, Nobel-speech confidence, and then the actual
follow-through arrives at the pace of a loading bar. Big announcement energy,
buffering-grade delivery.

Run it yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
