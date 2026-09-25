"""
Sysadmin Tools — fill in the four functions below.

Real parsing/decision logic behind what Lessons 2 and 4 describe doing by
eye: converting between permission notations, parsing `free -h`-style
output, and deciding which boot services are safe to disable. The swap
figures match the Terminal Simulator's Scenario 2 exactly.

Run the tests as you go:  pytest exercises/test_sysadmin_tools.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def octal_from_symbolic(perm_str):
    """Convert a symbolic permission string (e.g. "rwxr-xr-x") to its octal
    form (e.g. "755") -- the two notations `chmod` accepts, and the actual
    translation between them Lesson 2 describes.

    Each rwx triplet maps to a digit: r=4, w=2, x=1, summed per position.

    >>> octal_from_symbolic("rwxr-xr-x")
    '755'
    >>> octal_from_symbolic("rw-r--r--")
    '644'
    """
    # TODO: split perm_str into three 3-character groups (owner/group/other),
    # sum 4/2/1 for each present r/w/x in a group, and join the three
    # resulting digits into a string.
    raise NotImplementedError


def parse_size_to_mb(size_str):
    """Parse a human-readable size like "812Mi" or "1.0Gi" into a plain
    number of MB. Ki/Mi/Gi are binary units: 1Gi = 1024Mi, 1Mi = 1024Ki.

    This is the actual parsing `free -h` output needs before you can do
    any arithmetic on it.

    >>> parse_size_to_mb("812Mi")
    812.0
    >>> parse_size_to_mb("1.0Gi")
    1024.0
    """
    # TODO: strip the unit suffix (Ki/Mi/Gi), parse the numeric part as a
    # float, and scale it to MB (Ki -> /1024, Mi -> as-is, Gi -> *1024).
    raise NotImplementedError


def swap_pressure_pct(used_str, total_str):
    """What percentage of swap is in use, given human-readable used/total
    strings. Reuse parse_size_to_mb() rather than parsing twice.

    Matches the Terminal Simulator's Scenario 2 numbers: 812Mi used of
    1024Mi total swap.

    >>> round(swap_pressure_pct("812Mi", "1024Mi"), 1)
    79.3
    """
    # TODO: return parse_size_to_mb(used_str) / parse_size_to_mb(total_str) * 100
    raise NotImplementedError


def services_to_disable(enabled_services, essential_services):
    """Given the list of currently-enabled boot services and a list of
    services considered essential, return the ones that are enabled but
    NOT essential -- the actual audit from Lesson 3, as a function.

    >>> services_to_disable(["ssh", "bluetooth", "cron", "cups"], ["ssh", "cron"])
    ['bluetooth', 'cups']
    """
    # TODO: return the enabled_services not present in essential_services,
    # preserving their original order
    raise NotImplementedError
