from collections import Counter

from day_two.day_two_test_data import EXPECTED_PAYLOAD
from aoc_utils import get_dataset_from_url

import os
import requests


def checksum_generator(data):
    data_dict = {
        2: 0,
        3: 0,
    }
    for label in data:
        totals = Counter(label)
        for num in [2, 3]:
            if num in totals.values():
                data_dict[num] += 1
    return data_dict[2] * data_dict[3]


if __name__ == '__main__':
    URL='https://adventofcode.com/2018/day/2/input'

    LABEL_DATA = get_dataset_from_url(URL)
    CHECKSUM = checksum_generator(LABEL_DATA)
    print(CHECKSUM)  # 454
