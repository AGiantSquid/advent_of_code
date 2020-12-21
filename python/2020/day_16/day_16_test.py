'''
Demonstrates that code works for day 16.
'''
import pytest

from aoc_utils import get_aoc_data_for_challenge
from day_16 import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

DATA = [
    'class: 1-3 or 5-7',
    'row: 6-11 or 33-44',
    'seat: 13-40 or 45-50',
    '',
    'your ticket:',
    '7,1,14',
    '',
    'nearby tickets:',
    '7,3,47',
    '40,4,50',
    '55,2,20',
    '38,6,12',
]


def test_part_1():
    res = part_1(DATA)
    assert res == 71


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 24021


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 1289178686687


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
