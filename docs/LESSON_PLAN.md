# 📖 Lesson Plan — Linux-On-Old-Hardware

> **Chain K — Hardware & Systems Foundations** | Revive old machines with Linux: lightweight distros, the command line, services, and squeezing life out of limited resources.

## What This Project Is

Bring an old machine back to usefulness with Linux, learning administration under real resource constraints.

## Learning Objectives

By the end I can:

1. Choose a distribution deliberately for the hardware you have.
2. Work confidently in the shell: navigation, permissions, processes.
3. Manage services with systemd and control what starts at boot.
4. Diagnose memory, CPU, and disk pressure with standard tools.
5. Use a package manager and resolve dependency problems.
6. Recover a machine that will not boot.

## Software You Will Use

- A lightweight distro (Debian, Xubuntu, Alpine).
- A bootable USB.
- An old laptop or desktop.

## Build Order

1. Assess the hardware and pick a suitable distro.
2. Install it and get to a working desktop or console.
3. Audit what is running at boot; disable what is unnecessary.
4. Measure memory and CPU under normal use.
5. Install and run something genuinely useful on it.
6. Deliberately break the boot, then repair it from rescue media.

## Common Mistakes to Avoid

- Installing a heavy desktop environment on limited RAM.
- Running everything as root.
- Enabling services you do not need and never checking.
- Not knowing how to read `top`, `df`, or `journalctl`.
- No recovery plan before experimenting.

## Check Your Understanding

The quiz covers distro selection, systemd basics, diagnosing resource pressure, and boot recovery.

## Why This Matters (Industry Application)

Linux fluency is assumed for backend, DevOps, and data engineering work — servers run Linux and you'll
live in a terminal. Learning it under resource constraints builds better instincts than learning it on
hardware where nothing ever strains.

## Reflection Questions

- What made this machine 'too slow' before, and was that ever really true?
- Which shell skills here will you use most on a production server?
