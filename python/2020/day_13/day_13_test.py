'''
Demonstrates that code works for day 13.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_13 import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

DATA = [
    '939',
    '7,13,x,x,59,x,31,19',
]


def test_part_1():
    res = part_1(DATA)
    assert res == 295


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 0
