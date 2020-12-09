'''
Demonstrates that code works for day 9.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_9 import get_unsummable_num, get_contiguous_min_max_sum
PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    '35',
    '20',
    '15',
    '25',
    '47',
    '40',
    '62',
    '55',
    '65',
    '95',
    '102',
    '117',
    '150',
    '182',
    '127',
    '219',
    '299',
    '277',
    '309',
    '576',
]


def test_get_unsummable_num():
    res = get_unsummable_num(data, 5)
    assert res == 127


def test_get_unsummable_num_pd():
    res = get_unsummable_num(PUZZLE_DATA)
    assert res == 21806024


def test_get_contiguous_min_max_sum():
    res = get_contiguous_min_max_sum(data, get_unsummable_num(data, 5))
    assert res == 62


def test_get_contiguous_min_max_sum_pd():
    target = get_unsummable_num(PUZZLE_DATA)
    res = get_contiguous_min_max_sum(PUZZLE_DATA, target)
    assert res == 2986195
