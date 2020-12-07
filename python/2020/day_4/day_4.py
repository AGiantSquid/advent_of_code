#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 4.
'''
from functools import reduce
from typing import List

from aoc_utils import get_aoc_data_for_challenge


PASSPORT_FIELDS = {
    'byr': 'Birth Year',
    'iyr': 'Issue Year',
    'eyr': 'Expiration Year',
    'hgt': 'Height',
    'hcl': 'Hair Color',
    'ecl': 'Eye Color',
    'pid': 'Passport ID',
    'cid': 'Country ID',
}

REQUIRED_KEYS = [_ for _ in PASSPORT_FIELDS.keys() if _ != 'cid']


def to_dict(data: str) -> dict:
    d = {
        k: v
        for k, v in
        [_.split(':') for _ in data.split(' ')]
    }

    return d


def valid_passport(passport: dict) -> bool:
    keys = passport.keys()
    return not any([_ not in keys for _ in REQUIRED_KEYS])


def valid_passport_count(data: List[str]) -> int:
    def reducer(accum, el):
        # print(accum, el)
        if not accum:
            d = to_dict(el)
            return (d,)

        if not el:
            return accum + ({},)

        last_el = accum[-1]

        if not last_el:
            return accum[:-1] + (to_dict(el),)

        thing = {
            **last_el,
            **to_dict(el),
        }

        return accum[:-1] + (thing,)

    passport_data = reduce(reducer, data, tuple())

    return len([_ for _ in passport_data if valid_passport(_)])


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = valid_passport_count(puzzle_data)
    print(result)  # 219
