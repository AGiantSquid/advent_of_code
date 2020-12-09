'''
Demonstrates that code works for day 8.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_8 import get_total_at_repeat, get_total

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6',
]


def test_get_total_at_repeat():
    res = get_total_at_repeat(data)
    assert res == 5


def test_get_total_at_repeat_pd():
    res = get_total_at_repeat(PUZZLE_DATA)
    assert res == 1487


def test_get_total():
    res = get_total(data)
    assert res == 8


def test_get_total_pd():
    res = get_total(PUZZLE_DATA)
    assert res == 1607
