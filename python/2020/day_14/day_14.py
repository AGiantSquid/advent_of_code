#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 14.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge
from python_utils.sequence_utils import unpack_apply


def part_1(data: List[str]):
    mask = get_mask_val(data[0])
    d = {}

    for _ in data[1:]:
        if _.startswith('mask'):
            mask = get_mask_val(_)
            continue
        k, v = unpack_apply(_.split(' = '), get_mem_loc, str_to_bit_str)
        d[k] = apply_mask(mask, v)

    return sum(map(bit_str_to_int, d.values()))


def get_mask_val(x: str) -> str:
    return x.split(' = ')[1]


def get_mem_loc(x: str) -> str:
    return x[4:][:-1]


def str_to_bit_str(x: str) -> str:
    int_x = int(x)
    return int_to_bit_str(int_x)


def int_to_bit_str(x: int) -> str:
    return f'{x:036b}'


def bit_str_to_int(x: str) -> int:
    a = int(x, 2)
    return int(x, 2)


def apply_mask(x, y):
    y_arr = list(y)
    for i, el in enumerate(x):
        if el != 'X':
            y_arr[i] = el
    return ''.join(y_arr)

from itertools import chain

def part_2(data: List[str]):
    mask = get_mask_val(data[0])
    d = {}

    for line in data[1:]:
        if line.startswith('mask'):
            mask = get_mask_val(line)
            continue
        k, v = unpack_apply(line.split(' = '), get_mem_loc)
        new_keys = apply_mask_2(mask, str_to_bit_str(k))
        for num in new_keys:
            d[num] = v

    return sum(map(int, d.values()))


def apply_mask_2(mask: str, addr: str):
    addr_list = [list(addr)]
    for i, el in enumerate(mask):
        if el == '1':
            for j in addr_list:
                j[i] = '1'
            continue
        if el == 'X':
            for j in addr_list:
                j[i] = '1'
            copy = [_[:] for _ in addr_list]
            for j in addr_list:
                j[i] = '0'
            addr_list = addr_list + copy

    return [bit_str_to_int(''.join(_)) for _ in addr_list]


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)  # 9967721333886

    result = part_2(puzzle_data)
    print(result)  # 4355897790573
