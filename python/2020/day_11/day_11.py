#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 11.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def part_1(data: List[str]) -> int:
    final = get_equilibrium(data, draw_new_map)
    return count_occupied(final)


def get_equilibrium(data: List[str], draw_map_func):
    old_data = data
    while True:
        new_data = draw_map_func(old_data)
        if new_data == old_data:
            return new_data
        old_data = new_data


def draw_new_map(data: List[str]) -> List[str]:
    new_map = [['.' for seat in row] for row in data]

    for r, row in enumerate(data):
        for s, seat in enumerate(row):
            if seat == 'L':
                occupied = count_adjacent_occupied(data, r, s)
                if occupied == 0:
                    new_map[r][s] = '#'
                    continue

            if seat == '#':
                occupied = count_adjacent_occupied(data, r, s)
                if occupied >= 4:
                    new_map[r][s] = 'L'
                    continue

            new_map[r][s] = seat
    return [''.join(_) for _ in new_map]


def count_adjacent_occupied(data: List[str], x: int, y: int) -> int:
    adj_coords = get_adjacent_coords(x, y)
    count = 0
    for x, y in adj_coords:
        if x >= 0 and y >= 0:
            try:
                if data[x][y] == '#':
                    count += 1
            except IndexError:
                pass
    return count


def get_adjacent_coords(x, y):
    for x_offset in [-1, 0, 1]:
        for y_offset in [-1, 0, 1]:
            if x_offset == y_offset == 0:
                continue
            yield (x + x_offset, y + y_offset)


def count_occupied(data: List[str]) -> int:
    return len([seat for row in data for seat in row if seat == '#'])


def part_2(data: List[str]) -> int:
    final = get_equilibrium(data, draw_new_map_2)
    return count_occupied(final)


def draw_new_map_2(data: List[str]) -> List[str]:
    new_map = [['.' for seat in row] for row in data]

    for r, row in enumerate(data):
        for s, seat in enumerate(row):
            if seat == 'L':
                occupied = check_for_occupied_in_sight(data, r, s)
                if occupied == 0:
                    new_map[r][s] = '#'
                    continue
            if seat == '#':
                occupied = check_for_occupied_in_sight(data, r, s)
                if occupied >= 5:
                    new_map[r][s] = 'L'
                    continue
            new_map[r][s] = seat

    return [''.join(_) for _ in new_map]


def check_for_occupied_in_sight(data: List[str], x: int, y: int) -> int:
    count = 0

    for x_offset in [-1, 0, 1]:
        for y_offset in [-1, 0, 1]:
            if x_offset == y_offset == 0:
                continue
            new_x = x_offset + x
            new_y = y_offset + y

            while True:
                if new_x < 0 or new_y < 0:
                    break
                try:
                    seat = data[new_x][new_y]
                    if seat == 'L':
                        break
                    if seat == '#':
                        count += 1
                        break
                except IndexError:
                    break
                new_x += x_offset
                new_y += y_offset

    return count


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 2299

    result = part_2(puzzle_data)
    print(result)  # 2047
