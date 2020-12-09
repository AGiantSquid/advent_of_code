#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 6.
'''
from functools import reduce
from typing import Tuple, List
from aoc_utils import get_aoc_data_for_challenge


def sum_of_responses(data: List[str], unique=True) -> int:
    '''Return sum of responses from each cluster.'''
    if unique:
        sets_of_answers = get_sets_of_answers(data)
    else:
        sets_of_answers = get_sets_of_unanimous_answers(data)

    return sum([len(_) for _ in sets_of_answers])


def get_sets_of_answers(data: List[str]) -> Tuple[set, ...]:
    def reducer(accum, el):
        if not el:
            return accum + (set(),)

        return accum[:-1] + (accum[-1] | set(el),)

    return reduce(reducer, data, (set(),))


def get_sets_of_unanimous_answers(data: List[str]) -> Tuple[set, ...]:
    def reducer(accum, el):
        if not el:
            return accum + (None,)

        last_el = accum[-1]

        if last_el is None:
            return accum[:-1] + (set(el),)

        return accum[:-1] + (last_el & set(el),)

    return reduce(reducer, data, (None,))



if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = sum_of_responses(puzzle_data)
    print(result)  # 6534

    result = sum_of_responses(puzzle_data, unique=False)
    print(result)  # 3402
