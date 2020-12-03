from aoc_utils import get_aoc_data_for_challenge
from day_3 import get_overlapping_fabric


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
