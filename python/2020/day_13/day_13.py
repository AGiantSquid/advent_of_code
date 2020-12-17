#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 13.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def part_1(data: List[str]):
    time = int(data[0])
    busses = [int(_) for _ in data[1].split(',') if _ != 'x']

    times = {
        _ - (time % _): _
        for _ in busses
    }

    bus_id = min(times.keys())
    return bus_id * times[bus_id]


def part_2(data: List[str]):
    pass


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 2298

#    result = part_2(puzzle_data)
#    print(result)
