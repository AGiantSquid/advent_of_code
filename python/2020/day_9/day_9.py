#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 9.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def get_unsummable_num(data: List[str], preamble=25):
    data = [int(_) for _ in data]

    for i, el in enumerate(data[preamble:]):
        pool = data[i:preamble+i]
        res = summer(pool, el)
        if res is None:
            return el


def summer(pool, target):
    for i, el in enumerate(pool):
        for j, el2 in enumerate(pool):
            if i != j and el != el2:
                if el + el2 == target:
                    return el, el2


def get_contiguous_min_max_sum(data, target):
    data = [int(_) for _ in data]

    for i in range(len(data)):
        total = 0
        collection = []
        for j in range(i, len(data)):
            while total < target:

                item_to_add = data[j]
                total += item_to_add
                collection.append(item_to_add)

                if total == target:
                    return min(collection) + max(collection)

                j += 1


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result_1 = get_unsummable_num(puzzle_data)
    print(result_1)  # 21806024

    result2 = get_contiguous_min_max_sum(puzzle_data, result_1)
    print(result2)  # 2986195
