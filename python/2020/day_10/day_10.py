#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 10.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def process_data(data: List[str]) -> List[int]:
    '''convert strings to ints, add start and end items, and sort.'''
    ints = [int(_) for _ in data]

    max_num = max(ints)
    built_in_apapter = max_num + 3

    return sorted([0] + ints + [built_in_apapter])


def part_1(data: List[str]):
    d = process_data(data)

    ones = 0
    threes = 0

    for i, el in enumerate(d):
        if i == len(d) - 1:
            break
        if d[i + 1] - el == 1:
            ones += 1
            continue
        if d[i + 1] - el == 3:
            threes += 1

    return ones * threes


def part_2_naive(data: List[str]):
    '''Traverse all paths recursively.

    This function is prohibitively expensive, and is only used to check alternate strategies.'''
    d = process_data(data)
    return navigate(0, d, 0)


def navigate(i, data, count):
    '''Naively traverse all paths in a recursive fashion.'''
    goal = data[-1]

    curr = data[i]
    if curr == goal:
        return count

    if goal - curr <= 3 :
        count += 1

    for j in range(1, 4):
        try:
            next_el = data[i + j]
        except:
            continue

        if next_el - curr <= 3:
            count = navigate(i + j, data, count)

    return count


def part_2(data):
    '''Create dict to store all valid prior connections to each node, and accumulate total.'''
    d = process_data(data)

    paths = {d[0]: 1}

    for x in d[1:]:
        sum_of_paths = 0
        for y in range(1, 4):
            sum_of_paths += paths.get(x - y, 0)

        paths[x] = sum_of_paths

    return paths[d[-1]]


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 2112

    result = part_2(puzzle_data)
    print(result)  # 3022415986688
