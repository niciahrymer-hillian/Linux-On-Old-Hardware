"""
Tests for sysadmin_tools.py. Swap figures match the Terminal Simulator's
Scenario 2 exactly (812Mi used of 1024Mi total).
"""
import pytest

from sysadmin_tools import (
    octal_from_symbolic,
    parse_size_to_mb,
    swap_pressure_pct,
    services_to_disable,
)


def test_octal_from_symbolic_755():
    assert octal_from_symbolic("rwxr-xr-x") == "755"


def test_octal_from_symbolic_644():
    assert octal_from_symbolic("rw-r--r--") == "644"


def test_octal_from_symbolic_600():
    assert octal_from_symbolic("rw-------") == "600"


def test_parse_size_to_mb_mi():
    assert parse_size_to_mb("812Mi") == pytest.approx(812.0)


def test_parse_size_to_mb_gi():
    assert parse_size_to_mb("1.0Gi") == pytest.approx(1024.0)


def test_parse_size_to_mb_ki():
    assert parse_size_to_mb("2048Ki") == pytest.approx(2.0)


def test_swap_pressure_pct_matches_scenario_2():
    assert swap_pressure_pct("812Mi", "1024Mi") == pytest.approx(79.3, abs=0.1)


def test_swap_pressure_pct_zero_used():
    assert swap_pressure_pct("0Mi", "1024Mi") == pytest.approx(0.0)


def test_services_to_disable_matches_docstring():
    assert services_to_disable(["ssh", "bluetooth", "cron", "cups"], ["ssh", "cron"]) == ["bluetooth", "cups"]


def test_services_to_disable_nothing_to_disable():
    assert services_to_disable(["ssh", "cron"], ["ssh", "cron"]) == []
