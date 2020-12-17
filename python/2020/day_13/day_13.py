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


def part_2_naive(data: List[str]):
    busses = {
        int(el): i
        for i, el in enumerate(data[1].split(','))
        if el != 'x'
    }
    incrementor = max(busses.keys())

    inc_diff = busses[incrementor]

    busses = {
        k: v - inc_diff
        for k, v in busses.items()
    }

    for k, v in busses.items():
        if v > 0:
            busses[k] = v - k
    pos = incrementor
    valid = False
    while not valid:
        for k, v in busses.items():
            needed_offset = busses[k]

            observed_offset = (pos % k) * -1

            if needed_offset == observed_offset:
                valid = True
                continue

            pos += incrementor
            valid = False
            break

        if valid is True:
            return pos + busses[list(busses.keys())[0]]

    return busses


def part_2(data: List[str]):
    busses = {
        int(el): -i % int(el)
        for i, el in enumerate(data[1].split(','))
        if el != 'x'
    }

    iterator = 0
    increment = 1
    for bus, adj_offset in busses.items():
        while iterator % bus != adj_offset:
            iterator += increment
        increment *= bus

    return iterator


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 2298

    result = part_2(puzzle_data)
    print(result)  # 783685719679632
