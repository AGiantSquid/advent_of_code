'''
Demonstrates that code works for day 12.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_12 import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    'F10',
    'N3',
    'F7',
    'R90',
    'F11',
]


def test_part_1():
    res = part_1(data)
    assert res == 25


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 1603


def test_part_2():
    res = part_2(data)
    assert res == 286


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 52866
