#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 2.
'''
from collections import Counter
from typing import List

from aoc_utils import get_aoc_data_for_challenge


def password_checker_range(passwords: List[str]) -> int:
    '''Check if password contains a valid number of letters'''
    valid = 0
    for p in passwords:
        policy, letter_section, password = p.split(' ')
        letter = letter_section[0]
        minimum, maximum = [int(_) for _ in policy.split('-')]

        c = Counter(password)
        letter_count = c[letter]

        if letter_count >= minimum and letter_count <= maximum:
            valid += 1

    return valid


def password_checker_index(passwords: List[str]) -> int:
    '''Check if password has letters at proper index.'''
    valid = 0
    for p in passwords:
        policy, letter_section, password = p.split(' ')
        letter = letter_section[0]
        i1, i2 = [int(_) - 1 for _ in policy.split('-')]

        c = Counter([password[i1], password[i2]])

        if c[letter] == 1:
            valid += 1

    return valid


if __name__ == '__main__':
    data = get_aoc_data_for_challenge(__file__)

    result = password_checker_range(data)
    print(result)  # 474

    result_2 = password_checker_index(data)
    print(result_2)  # 745
