#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 5.
'''
from typing import Tuple, List
from aoc_utils import get_aoc_data_for_challenge

ROWS = 128
COLUMNS = 8


def highest_id(data: List[str]) -> int:
    return max([get_seat_id(_) for _ in data])


def get_seat_id(data: str) -> int:
    row, col = get_row_column(data)
    return row * 8 + col


def get_row_column(data: str) -> Tuple[int, int]:
    '''Parse data to get row and column number.'''
    row = get_row(data)
    column = get_column(data)

    return (row, column)


def get_row(data: str):
    low = 0
    high = ROWS - 1
    row_data = data[:7]
    for r in row_data:
        bottom, top = get_bottom_top(low, high)
        if r == 'F':
            low, high = bottom
        else:
            low, high = top
    return low


def get_column(data: str):
    low = 0
    high = COLUMNS - 1
    col_data = data[7:]
    for c in col_data:
        bottom, top = get_bottom_top(low, high)
        if c == 'L':
            low, high = bottom
        else:
            low, high = top
    return low


def get_bottom_top(low: int, high: int) -> Tuple[Tuple[int, int], ...]:
    range = high - low
    half = range // 2
    return ((low, low + half), (high - half, high))


def find_missing_middle_seat(data: str) -> int:
    all_ids = sorted([get_seat_id(_) for _ in data])
    all_ids_set = set(all_ids)

    for i in range(all_ids[0], all_ids[-1]):
        if i not in all_ids_set:
            return i


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__)

    result = highest_id(puzzle_data)
    print(result)  # 928

    result = find_missing_middle_seat(puzzle_data)
    print(result)  # 610
