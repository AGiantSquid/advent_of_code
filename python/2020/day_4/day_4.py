#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 4.
'''
import re
from functools import reduce
from typing import List

from aoc_utils import get_aoc_data_for_challenge


def range_validator(low, high):
    def wrapped(x):
        return low <= int(x) <= high
    return wrapped


def valid_height(x):
    if len(x) <= 2:
        return False
    if x.endswith('cm'):
        return range_validator(150, 193)(x[:-2])
    return range_validator(59, 76)(x[:-2])


def valid_hair(x):
    return len(x) == 7 and re.match(r'#[a-f0-9]{6}', x) is not None


def valid_eye(x):
    return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_pid(x):
    return len(x) == 9 and x.isdigit()


PASSPORT_FIELDS = {
    'byr': range_validator(1920, 2002),
    'iyr': range_validator(2010, 2020),
    'eyr': range_validator(2020, 2030),
    'hgt': valid_height,
    'hcl': valid_hair,
    'ecl': valid_eye,
    'pid': valid_pid,
    'cid': lambda x: True,
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


def valid_passport_2(passport: dict) -> bool:
    keys = passport.keys()
    missing_keys = any([_ not in keys for _ in REQUIRED_KEYS])

    if missing_keys:
        return False

    return all([
        PASSPORT_FIELDS[k](v)
        for k, v in passport.items()
    ])


def valid_passport_count(data: List[str], validator: callable) -> int:
    def reducer(accum, el):
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

    return len([_ for _ in passport_data if validator(_)])




if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = valid_passport_count(puzzle_data, valid_passport)
    print(result)  # 219

    result = valid_passport_count(puzzle_data, valid_passport_2)
    print(result)  # 127
