# Make the best-looking food picture — make.fun bounty food-picture-01

A steaming bowl of tonkotsu ramen: chopsticks lifting glossy noodles
from a rich creamy broth, a halved jammy egg with a golden runny yolk,
tender chashu pork, green onions and nori, steam in warm window light
on a dark wooden table.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png`
(the image held in this repository) to `/output/entry.png`. No
network, no randomness, no clock — two runs write identical bytes.

`entry.png` is 1024×1024 and under 1 MiB.

## Run it

```sh
python3 main.py   # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # local run, writes out/entry.png
```

## License

MIT — see LICENSE.
