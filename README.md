# World news, Thursday 19 November 2026 — in one image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Hizmaelgzz/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Hizmaelgzz/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun competition
[`news-image-20261119`](https://make.fun/bounty/news-image-20261119):
sum up 19 November 2026's world news in a single image.

## The image

`entry.png` is a newspaper front page — masthead **WORLD NEWS**,
dateline **THURSDAY 19 NOVEMBER 2026**, and six panels covering the
day's most consequential stories, as reported on 19 November 2026:

1. **Trump, Xi and Putin meet in Shenzhen** — the trilateral summit
   in China, with Ukraine, Iran, energy and nuclear arms control on
   the agenda.
2. **GTA VI launches worldwide** — the global rollout of the year's
   biggest video-game release.
3. **World Court rules on Myanmar genocide case** — the ICJ verdict
   on the Rohingya genocide case against Myanmar.
4. **Tankers hit mines near Strait of Hormuz** — three oil tankers
   catch fire after hitting mines east of the strait.
5. **Israeli tanks advance in Gaza** — a rare ground operation
   beyond the ceasefire line.
6. **Voyager 1 reaches one light-day** — NASA's probe passes the
   one-light-day milestone from Earth.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png`
to the output directory. It needs no network, so two runs write
identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
