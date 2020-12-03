#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 3.
'''
from functools import reduce
from operator import mul

from aoc_utils import get_aoc_data_for_challenge


def prod(list_of_ints):
    '''Return the product of list of ints.

    This method is built into numpy,
    but recreated here to keep imports light.'''
    return reduce(mul, list_of_ints)


def get_trees_hit_part_1(data):
    '''Calculate trees hit moving right 3 spaces.'''
    return calculate_trees_hit(data, 3, 1)


def get_trees_hit_part_2(data):
    '''Calculate trees hit with multiple strategies.'''
    strategies = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    return prod([calculate_trees_hit(data, *_) for _ in strategies])


def calculate_trees_hit(data, x, skip=1):
    '''Calculate trees hit with variable moves.'''
    trees_hit = 0

    position = 0
    for i, el in enumerate(data):
        if i == 0:
            continue
        if skip > 1 and i % skip != 0:
            continue
        position += x
        while position >= len(el):
            el = el + el
        coor = el[position]
        if coor == '#':
            trees_hit += 1

    return trees_hit


if __name__ == '__main__':
    pattern_data = get_aoc_data_for_challenge(__file__)

    result = get_trees_hit_part_1(pattern_data)
    print(result)  # 276

    result = get_trees_hit_part_2(pattern_data)
    print(result)  # 7812180000
