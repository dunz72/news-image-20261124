# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/dunz72/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/dunz72/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World in One Day — Tuesday 24 November 2026. A program that copies one 1024×1024 front page summing up the day's world news in one image: the ICJ's historic 9-6 ruling that Myanmar committed genocide against the Rohingya, COP31 collapsing in Antalya after 50 hours of overtime, Ukraine's naval drones sinking a Russian warship off Benghazi, Nvidia reinstating Jensen Huang as chief executive, and the capture of El Chapo Isidro with U.S. drone help — plus a footer strip on Nepal's 5.6 quake and the UN chief's call for global AI safety rules.

`main.py` is standard library only: it copies the pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, validates the PNG signature, the 1024×1024 IHDR dimensions, and the 1 MiB size limit, then verifies the copy byte-for-byte with SHA-256.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB). Running it twice produces identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rwrq8ddk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
