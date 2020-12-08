from aoc_utils import get_aoc_data_for_challenge
from day_6 import sum_of_unique_responses

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


def test_sum_of_unique_responses():
    res = sum_of_unique_responses(data)
    assert res == 11


def test_sum_of_unique_responses_pd():
    res = sum_of_unique_responses(PUZZLE_DATA)
    assert res == 6534
