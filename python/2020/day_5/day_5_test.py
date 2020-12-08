from aoc_utils import get_aoc_data_for_challenge
from day_5 import get_row_column, get_seat_id, highest_id, find_missing_middle_seat


PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    ['FBFBBFFRLR', 357],
    ['BFFFBBFRRR', 567],
    ['FFFBBBFRRR', 119],
    ['BBFFBBFRLL', 820],
]


def test_get_row_column():
    res = get_row_column(data[0][0])
    assert res == (44, 5)


def test_get_seat_id():
    for t in data:
        res = get_seat_id(t[0])
        assert res == t[1]


def test_highest_id():
    res = highest_id([_[0] for _ in data])
    assert res == 820


def test_highest_id_pd():
    res = highest_id(PUZZLE_DATA)
    assert res == 928


def test_find_missing_middle_seat():
    res = find_missing_middle_seat(PUZZLE_DATA)
    assert res == 610
