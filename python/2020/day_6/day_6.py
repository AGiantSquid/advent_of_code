#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 6.
'''
from functools import reduce
from typing import Tuple, List, Iterable
from aoc_utils import get_aoc_data_for_challenge, chunk_aoc_data


def sum_of_responses(data: List[str], unique=True) -> int:
    '''Return sum of responses from each cluster.'''
    chunked = chunk_aoc_data(data)

    if unique:
        sets_of_answers = get_unique_letters_in_chunks(chunked)
    else:
        sets_of_answers = get_common_letters_in_chunks(chunked)

    return sum([len(_) for _ in sets_of_answers])


def get_unique_letters_in_chunks(data: Tuple[Tuple[str]]) -> Iterable:
    '''Get set of unique individual letters in chunks.'''
    return (set(''.join(_)) for _ in data)


def get_common_letters_in_chunks(data: Tuple[Tuple[str]]) -> Iterable:
    '''Get set of common letters in chunks.'''
    sets = (
        (set(_) for _ in el)
        for el in data
    )

    return (reduce(lambda x, y: x & y, s) for s in sets)


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = sum_of_responses(puzzle_data)
    print(result)  # 6534

    result = sum_of_responses(puzzle_data, unique=False)
    print(result)  # 3402
