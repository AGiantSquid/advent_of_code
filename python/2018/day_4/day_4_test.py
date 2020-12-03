from aoc_utils import get_aoc_data_for_challenge
from day_4 import get_product_of_guard_id_and_minute, get_product_of_guard_id_and_minute_2


PUZZLE_INPUT = get_aoc_data_for_challenge(__file__)


data = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up',
]

def test_get_product_of_guard_id_and_minute():
    res = get_product_of_guard_id_and_minute(data)

    assert res == 240


def test_get_product_of_guard_id_and_minute_puzzle_input():
    res = get_product_of_guard_id_and_minute(PUZZLE_INPUT)

    assert res == 36898


def test_get_product_of_guard_id_and_minute_2():
    res = get_product_of_guard_id_and_minute_2(data)

    assert res == 4455


def test_get_product_of_guard_id_and_minute_2():
    res = get_product_of_guard_id_and_minute_2(PUZZLE_INPUT)

    assert res == 80711
