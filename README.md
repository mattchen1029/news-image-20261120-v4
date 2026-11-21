# The Day in World News: Friday 20 November 2026 — 46 stories, 7 regions, one page

A make.fun `news-image-20261120` entry. A pure-stdlib Python program draws a
1024x1024 newspaper front page summing up Friday 20 November 2026: 3
illustrated leads, 9 secondary stories, a BY THE NUMBERS strip, a UTC
timeline, 34 one-line briefs, and a sources line. Every story was verified
against reporting from 20 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024x1024 PNG, under 1 MiB). Two runs produce
byte-identical output. Standard library only, no network.

## Files

- `main.py` — story data and page layout
- `render.py` — pure-stdlib raster renderer, 5x7 bitmap font, PNG encoder
- `entry.png` — the rendered front page

## License

MIT
