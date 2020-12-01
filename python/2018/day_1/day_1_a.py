#!/usr/bin/env python3
from aoc_utils import get_dataset_from_url


def get_end_frequency(frequency_changes):
    """Sum numbers together to get result frequency."""
    return sum(int(num) for num in frequency_changes)


if __name__ == '__main__':
    URL='https://adventofcode.com/2018/day/1/input'

    FREQUENCY_LIST = get_dataset_from_url(URL)
    END_FREQUENCY = get_end_frequency(FREQUENCY_LIST)
    print(END_FREQUENCY)  # 454
