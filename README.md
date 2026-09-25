# Linux-On-Old-Hardware

### Revive old machines with Linux: lightweight distros, the command line, services, and squeezing life out of limited resources.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**. Builds on **Machine-Under-The-Hood** — the memory
hierarchy and I/O concepts there directly explain why swap pressure feels the way it does here.

## What this is

We're bringing an old, "too slow" machine back to real usefulness with Linux — and along the way,
learning administration under resource constraints that force real understanding instead of letting a
fast machine paper over what you don't actually know. A machine with 2-4GB of RAM won't tolerate a
careless desktop-environment choice or an unaudited pile of background services the way a modern machine
will. The four lessons build in the order you'd actually need them: pick a distro deliberately, get
comfortable in the shell, audit what's running at boot, then diagnose resource pressure and — the skill
most tutorials skip — recover a machine that won't boot at all. Practice all three of the hands-on
scenarios (service auditing, memory-pressure diagnosis, chroot-based recovery) in the **Terminal
Simulator** tab before you're doing it for real with no safety net.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| An old machine (optional) | Only needed for the hardware appendix — the tour and exercises need nothing but a browser and Python |

## Items Needed

- [ ] An old laptop or desktop (anything from the last ~10-15 years works)
- [ ] A USB drive (8GB+) for a bootable installer
- [ ] A second USB drive or the same one, for rescue/live media (Lesson 4's recovery practice)
- [ ] Nothing else — this project is entirely software/configuration, no parts to buy

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Distro & install) first.** If you have an old machine available, check its actual
   RAM/CPU before picking a distro and desktop environment — don't default to whatever you'd install on
   a modern machine.
3. **Work Lesson 2 (Command line)**, then open the **Terminal Simulator** tab and work through
   Scenario 1 (auditing and disabling unnecessary boot services).
4. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 10 failing tests. Open `exercises/sysadmin_tools.py` and implement the four functions —
   full instructions in [`exercises/README.md`](exercises/README.md).
5. **Work Lesson 3 (systemd)** — you'll have already done its hands-on part in step 3.
6. **Work Lesson 4 (Resource pressure & recovery)**, then Terminal Simulator Scenarios 2 and 3.
   > ⚠️ **You may get stuck here:** Scenario 3's third step (fixing the fstab entry) is **freeform** —
   > type anything describing the fix, it's not checking an exact string. The point is practicing the
   > mount → chroot → fix → exit → reboot sequence, not memorizing exact fstab syntax.
7. **Then the Quiz**, then Flashcards/Match/Pop Quiz for review.
8. **Check the Report Card tab** any time. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Terminal Simulator scenario |
|---|---|---|---|
| 1 | Distro & install | Lightweight distros, DE RAM cost | *(hardware appendix — no simulator scenario)* |
| 2 | Command line | Permissions, SIGTERM vs SIGKILL, root vs sudo | *(feeds directly into Scenario 1)* |
| 3 | systemd services | Auditing/disabling boot services | Scenario 1 — Audit & disable unnecessary boot services |
| 4 | Resource pressure & recovery | top/df/journalctl, swap pressure, chroot recovery | Scenarios 2 & 3 |

**Learning path:**
```
Lesson 1 (distro)  →  Lesson 2 (shell)  →  Lesson 3 (systemd)  →  Lesson 4 (pressure & recovery)
                              ↓                    ↓                          ↓
                    exercises/ (sysadmin_tools.py)  Terminal Sim: Scenario 1   Scenarios 2 & 3
                                                            ↓
                                          Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide

This project needs no new hardware — the entire point is reusing a machine you (or someone) already has
that's been written off as "too slow." If you don't have one available, any decade-plus-old laptop or
desktop from a family member, a local surplus sale, or an e-waste drop-off works fine for this project.

## Why This Matters (Industry Application)

Linux fluency is assumed for backend, DevOps, and data engineering work — servers run Linux and you'll
live in a terminal. Learning it under resource constraints builds better instincts than learning it on
hardware where nothing ever strains.

## How This Connects

Chain K (Hardware & Systems Foundations). Builds on **Machine-Under-The-Hood**; the shell skills feed
**Shell-And-Small-Software**.

## Project Layout

```
Linux-On-Old-Hardware/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, terminal sim, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page command/rule recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── sysadmin_tools.py        # skeleton — implement the 4 functions
│   ├── test_sysadmin_tools.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
