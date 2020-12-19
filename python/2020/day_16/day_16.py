#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 16.
'''
from itertools import chain
from typing import List

from aoc_utils import get_aoc_data_for_challenge, chunk_aoc_data
from python_utils.sequence_utils import unpack_apply


def part_1(data: List[str]):
    chunked = chunk_aoc_data(data)
    valid_ranges, _, nearby_ticket_vals = unpack_apply(chunked, get_valid_ranges, None, get_nearby_ticket_values)

    return sum(get_invalid_numbers(valid_ranges, nearby_ticket_vals))


def get_valid_ranges(x):
    ranges = chain.from_iterable([_.split(': ')[1].split(' or ') for _ in x])
    r = [[int(s) for s in _.split('-')] for _ in ranges]
    v = []
    s = sorted(r)
    for el in s:
        if not v:
            v.append(el)
            continue
        if el[0] > v[-1][1] + 1:
            v.append(el)
            continue
        if el[1] < v[-1][1]:
            continue
        v[-1][1] = el[1]

    return v


def get_invalid_numbers(valid_ranges, nearby_ticket_vals):
    invalid_numbers = []
    for val in nearby_ticket_vals:
        invalid = True
        for low, high in valid_ranges:
            if low <= val <= high:
                invalid = False
        if invalid:
            invalid_numbers.append(val)
    return invalid_numbers


def get_nearby_ticket_values(x):
    vals = chain.from_iterable([_.split(',') for _ in x[1:]])
    return list(map(int, vals))


def part_2(data: List[str]):
    pass


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)

    # result = part_2(puzzle_data)
    # print(result)
