#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 15.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def part_1(data: List[str], n=2020):
    data = [int(_) for _ in data[0].split(',')]
    turn = 0

    d = {}
    spoken = None

    while turn < n:
        if turn < len(data):
            spoken = data[turn]

        elif len(d[spoken]) == 1:
            spoken = 0

        else:
            spoken = d[spoken][-1] - d[spoken][-2]

        obs = d.get(spoken, [])
        obs.append(turn)
        d[spoken] = obs
        turn += 1
    return spoken

def part_2(data: List[str]):
    return part_1(data, 30000000)


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 492

    result = part_2(puzzle_data)
    print(result)  # 63644
