#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 1.
'''
from os.path import join, dirname
from typing import List, Tuple

from aoc_utils import get_dataset_from_url, read_cookies_from_file


def get_product_of_entries(nums: List[str]) -> int:
    '''Get the 2 elements from list that sum to 2020, and return product.'''
    entries = find_2020_entries(nums)
    return get_product(entries)


def find_2020_entries(nums: List[str]) -> Tuple[int, int]:
    '''Get the pair of elements that sum to 2020.'''
    nums_as_ints = [int(_) for _ in nums]

    for i, num in enumerate(nums_as_ints):
        for i2, num2 in enumerate(nums_as_ints):
            if i != i2 and num + num2 == 2020:
                return num, num2

    raise IOError('Input data does not contain numbers that match criteria')


def get_product(entries: Tuple[int, int]) -> int:
    return entries[0] * entries[1]


if __name__ == '__main__':
    url = 'https://adventofcode.com/2020/day/1/input'
    cookie_file = join(dirname(dirname(__file__)), 'cookies.txt')
    cookies = read_cookies_from_file(cookie_file)
    data = get_dataset_from_url(url, cookies)
    result = get_product_of_entries(data)

    print(result)
