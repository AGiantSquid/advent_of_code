#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 1.
'''
from os.path import join, dirname
from typing import List, Tuple
from functools import reduce

from aoc_utils import get_dataset_from_url, read_cookies_from_file


def get_product_of_entries(nums: List[str]) -> int:
    '''Get the 2 elements from list that sum to 2020, and return product.'''
    entries = find_2020_entries(nums)
    return get_product(entries)


def get_product_of_entries_three(nums: List[str]) -> int:
    '''Get the 3 elements from list that sum to 2020, and return product.'''
    entries = find_2020_entries_three(nums)
    return get_product(entries)


def find_2020_entries(nums: List[str]) -> Tuple[int, int]:
    '''Get the pair of elements that sum to 2020.'''
    nums_as_ints = [int(_) for _ in nums]
    sorted_ints = sorted(nums_as_ints)

    for i, num in enumerate(sorted_ints):
        for i2, num2 in enumerate(sorted_ints):
            if i != i2:
                sum_of_entries = num + num2
                if sum_of_entries == 2020:
                    return num, num2
                if sum_of_entries > 2020:
                    break

    raise IOError('Input data does not contain numbers that match criteria')


def find_2020_entries_three(nums: List[str]) -> Tuple[int, int, int]:
    '''Get the 3 elements that sum to 2020.'''
    nums_as_ints = [int(_) for _ in nums]
    sorted_ints = sorted(nums_as_ints)

    for i, num in enumerate(sorted_ints):
        for i2, num2 in enumerate(sorted_ints):
            if i != i2:
                first_sum = num + num2
                if first_sum > 2020:
                    break
                for i3, num3 in enumerate(sorted_ints):
                    if i != i3 and i2 != i3:
                        second_sum = first_sum + num3
                        if second_sum == 2020:
                            return num, num2, num3
                        if second_sum > 2020:
                            break

    raise IOError('Input data does not contain numbers that match criteria')


def get_product(entries: Tuple[int, ...]) -> int:
    '''Return the product of all elements.'''
    return reduce(lambda x, y: x * y, entries)


if __name__ == '__main__':
    url = 'https://adventofcode.com/2020/day/1/input'
    cookie_file = join(dirname(dirname(__file__)), 'cookies.txt')
    cookies = read_cookies_from_file(cookie_file)
    data = list(get_dataset_from_url(url, cookies))

    result = get_product_of_entries(data)
    print(result)  # 987339

    result_2 = get_product_of_entries_three(data)
    print(result_2)  # 259521570
