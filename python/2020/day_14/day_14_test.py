'''
Demonstrates that code works for day 14.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_14 import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

DATA = [
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0',
]


def test_part_1():
    res = part_1(DATA)
    assert res == 165


def test_part_1_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 9967721333886


def test_part_2():
    data = [
        'mask = 000000000000000000000000000000X1001X',
        'mem[42] = 100',
        'mask = 00000000000000000000000000000000X0XX',
        'mem[26] = 1',
    ]
    res = part_2(data)
    assert res == 208


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 4355897790573
