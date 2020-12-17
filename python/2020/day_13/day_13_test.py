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


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 2298


def test_part_2():
    res = part_2(DATA)
    assert res == 1068781


def test_part_2a():
    data = [
        ['17,x,13,19', 3417],
        ['67,7,59,61', 754018],
        ['67,x,7,59,61', 779210],
        ['67,7,x,59,61', 1261476],
        ['1789,37,47,1889', 1202161486],
    ]

    for d in data:
        res = part_2(['', d[0]])
        assert res == d[1]


def test_part_2():
    res = part_2(PUZZLE_DATA)
    assert res == 783685719679632
