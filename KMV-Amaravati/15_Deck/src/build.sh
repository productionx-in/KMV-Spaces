#!/bin/sh
# Rebuild the deck from source. Run from this directory.
set -e
for p in a b c d e f g; do python3 dk_$p.py; done
cat deck_a.html deck_b.html deck_c.html deck_d.html deck_e.html deck_f.html deck_g.html > kmv-deck.html
python3 fitpage.py      # measures each slide and bakes a per-slide print scale
python3 dk_render.py    # renders desktop + mobile checks, writes kmv-deck.pdf
python3 dk_val.py       # 151 structural, arithmetic and language checks
