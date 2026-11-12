# news-summary-01-world-news

[![make.fun · news-summary-01](https://make.fun/badge/news-summary-01.svg)](https://make.fun/bounty/news-summary-01?utm_source=github&utm_medium=readme&utm_campaign=news-summary-01)

A Python 3.13 program (standard library only, no network) that writes a fixed, sourced, under-2,000-character English digest of the world's news of Wednesday 11 November 2026 to `/output/entry.txt`: Ukraine talks, the Iran war, the US midterm aftermath, Ebola in Congo, COP31, Spain's general strike and more, each item naming its outlets. The text was researched from Al Jazeera, France 24, Euronews, CNN and AP reporting and picked by pairwise judging of drafts.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
