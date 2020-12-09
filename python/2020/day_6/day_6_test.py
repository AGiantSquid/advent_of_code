from aoc_utils import get_aoc_data_for_challenge
from day_6 import sum_of_responses

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b',
]


def test_sum_of_responses():
    res = sum_of_responses(data)
    assert res == 11


def test_sum_of_responses_pd():
    res = sum_of_responses(PUZZLE_DATA)
    assert res == 6534


def test_sum_of_responses_common():
    res = sum_of_responses(data, unique=False)
    assert res == 6


def test_sum_of_responses_common_pd():
    res = sum_of_responses(PUZZLE_DATA, unique=False)
    assert res == 3402
