'''
Demonstrates that code works for day 15.
'''
import pytest

from aoc_utils import get_aoc_data_for_challenge
from day_15 import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)


def test_part_1():
    data = [
        ['0,3,6', 436],
        ['1,3,2', 1],
        ['2,1,3', 10],
        ['1,2,3', 27],
        ['2,3,1', 78],
    ]
    for t in data:
        res = part_1([t[0]])
        assert res == t[1]


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 492


@pytest.mark.slow
def test_part_2():
    data = ['0,3,6']

    res = part_2(data)
    assert res == 175594


@pytest.mark.slow
def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 63644
