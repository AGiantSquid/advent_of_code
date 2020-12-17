#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 12.
'''

from typing import List
from aoc_utils import get_aoc_data_for_challenge


def part_1(data: List[str]):
    starting_coords = (0, 0)
    orientation = 0
    for el in data:
        starting_coords, orientation = get_new_coords(starting_coords, orientation, el)

    return sum([abs(_) for _ in starting_coords])

def get_new_coords(starting_coords, orientation, move: str):
    directions = {
        'E': lambda c, d: (c[0] + d, c[1]),
        'S': lambda c, d: (c[0], c[1] - d),
        'W': lambda c, d: (c[0] - d, c[1]),
        'N': lambda c, d: (c[0], c[1] + d),
    }

    direction = move[0]
    num = int(move[1:])

    if direction == 'F':
        direction = list(directions.keys())[orientation]

    if direction in directions:
        return directions[direction](starting_coords, num), orientation

    num = num % 360

    if direction == 'L':
        num = 360 - num

    num = num // 90

    return starting_coords, (orientation + num) % 4


def part_2(data: List[str]):
    starting_coords = (0, 0)
    waypoint = (10, 1)
    for el in data:
        starting_coords, waypoint = get_new_coords_2(starting_coords, waypoint, el)

    return sum([abs(_) for _ in starting_coords])


def get_new_coords_2(starting_coords, waypoint, move: str):
    directions = {
        'E': lambda c, d: (c[0] + d, c[1]),
        'S': lambda c, d: (c[0], c[1] - d),
        'W': lambda c, d: (c[0] - d, c[1]),
        'N': lambda c, d: (c[0], c[1] + d),
    }

    r_turns = {
        90: lambda x, y: (y, x * -1,),
        180: lambda x, y: (x * -1, y * -1),
        270: lambda x, y: (y * -1, x),
    }

    direction = move[0]
    num = int(move[1:])

    if direction == 'F':
        ending_coords = (starting_coords[0] + (waypoint[0] * num), starting_coords[1] + (waypoint[1] * num))
        return ending_coords, waypoint

    if direction in directions:
        return starting_coords, directions[direction](waypoint, num)

    num = num % 360

    if direction == 'L':
        num = 360 - num

    return starting_coords, r_turns[num](*waypoint)


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 1603

    result = part_2(puzzle_data)
    print(result)  # 52866
