from aoc_utils import get_aoc_data_for_challenge
from day_3 import get_overlapping_fabric, get_non_overlapping_pattern_id


PUZZLE_INPUT = get_aoc_data_for_challenge(__file__)


def test_get_overlapping_fabric():
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]

    res = get_overlapping_fabric(data)

    assert res == 4


def test_get_overlapping_fabric_2():
    res = get_overlapping_fabric(PUZZLE_INPUT)

    assert res == 112418


def test_get_non_overlapping_pattern_id():
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]

    res = get_non_overlapping_pattern_id(data)

    assert res == '3'


def test_get_non_overlapping_pattern_id_2():
    res = get_non_overlapping_pattern_id(PUZZLE_INPUT)

    assert res == '560'
