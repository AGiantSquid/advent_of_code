from collections import Counter
from functools import reduce
from operator import mul

from day_2.day_2_test_data import EXPECTED_PAYLOAD
from aoc_utils import get_dataset_from_url

def prod(list_of_ints):
    """Prod returns the product of list of ints. This method is built into numpy,
    but recreated here to keep imports light."""
    return reduce(mul, list_of_ints, 1)

def checksum_generator(data):
    # count instances of all letters in each label, return "1" for labels that have 2 of any letter, or 3 of any letter,
    # sum the ones that have 2 and 3, then multiply them.
    return prod([sum([1 for label in data if num in Counter(label).values()]) for num in [2,3]])


if __name__ == '__main__':
    URL='https://adventofcode.com/2018/day/2/input'

    LABEL_DATA = get_dataset_from_url(URL)
    CHECKSUM = checksum_generator(LABEL_DATA)
    print(CHECKSUM)  # 454
