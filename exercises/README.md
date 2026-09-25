# Exercises — Sysadmin Tools

A hands-on companion to Lessons 2 and 4 in the interactive tour: real parsing and decision logic behind
what those lessons describe doing by eye — converting permission notations, parsing `free -h`-style
output, and auditing which boot services are safe to disable.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 10 failing tests — every function in `sysadmin_tools.py` currently raises
`NotImplementedError`.

## What to do

Open `sysadmin_tools.py`. Implement in this order:

1. `octal_from_symbolic` — convert `rwxr-xr-x` style permissions to `755` style, the two notations
   `chmod` accepts.
2. `parse_size_to_mb` — parse `free -h`'s human-readable sizes (`812Mi`, `1.0Gi`) into plain MB numbers.
3. `swap_pressure_pct` — reuse `parse_size_to_mb` to compute swap usage as a percentage. Matches the
   Terminal Simulator's Scenario 2 numbers exactly (812Mi of 1024Mi).
4. `services_to_disable` — the actual audit logic from Lesson 3: which enabled services aren't on your
   essential list.

## When you're done

All 10 tests passing means you have real, reusable tools for exactly the kind of manual work this
project asks you to do by hand on real hardware — parsing memory pressure and auditing services aren't
just things to eyeball once, they're things worth having a script for.
