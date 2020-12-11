'''
Demonstrates that code works for day 10.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_10 import part_1, part_2_naive, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data_1 = [
    '16',
    '10',
    '15',
    '5',
    '1',
    '11',
    '7',
    '19',
    '6',
    '12',
    '4',
]

data_2 = [
    '28',
    '33',
    '18',
    '42',
    '31',
    '14',
    '46',
    '20',
    '48',
    '47',
    '24',
    '23',
    '49',
    '45',
    '19',
    '38',
    '39',
    '11',
    '1',
    '32',
    '25',
    '35',
    '8',
    '17',
    '7',
    '9',
    '4',
    '2',
    '34',
    '10',
    '3',
]


def test_part_1_a():
    res = part_1(data_1)
    assert res == 35


def test_part_1_b():
    res = part_1(data_2)
    assert res == 220


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 2112


def test_part_2_naive_a():
    res = part_2_naive(data_1)
    assert res == 8


def test_part_2_naive_a():
    res = part_2_naive(data_2)
    assert res == 19208


def test_part_2():
    res = part_2(data_1)
    assert res == 8


def test_part_2():
    res = part_2(data_2)
    assert res == 19208


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 3022415986688
