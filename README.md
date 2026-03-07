# Project Island — Contestant Generator

This repository contains a lightweight contestant generator inspired by the Total Drama reality-show style for the Project Island game/contest.

What this adds
- A small Python generator (`generator.py`) that produces contestants with names, ages, and genders.
- Data files for first names and surnames in `data/`.
- A sample output in `outputs/sample_contestants.json`.

Quick start

Requirements
- Python 3.8+

Generate 8 contestants (default):

```bash
python generator.py --count 8 --seed 42 --output outputs/contestants.json
```

Specify genders in order (comma-separated):

```bash
python generator.py -c 6 -g "female,male,non-binary,male,female,non-binary"
```

Files created
- `generator.py` — the generator script
- `data/names.json` — lists of first names (male/female/neutral)
- `data/surnames.json` — list of surnames
- `outputs/sample_contestants.json` — example generated output
- `.gitignore`

License
- Add a license if you want to release this publicly.
