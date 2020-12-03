#!/usr/bin/env python3
from collections import Counter
from functools import reduce
from operator import mul

from aoc_utils import get_aoc_data_for_challenge


def prod(list_of_ints):
    '''Return the product of list of ints.

    This method is built into numpy,
    but recreated here to keep imports light.'''
    return reduce(mul, list_of_ints)


def checksum_generator(data):
    '''Count instances of all letters in each label,

    Return "1" for labels that have 2 of any letter, or 3 of any letter,
    Sum the ones that have 2 and 3, then multiply them.'''
    return prod([
        sum([
            1 for label in data
            if num in Counter(label).values()
        ])
        for num in [2, 3]
    ])


def common_letters_in_correct_labels(data):
    '''Return list of common letters from labels that match all letters but one.'''
    res = []
    for i, label in enumerate(data):
        for compare_label in data:
            letter_diff, same_letters = letter_difference(label, compare_label)
            if letter_diff == 1:
                res.append(same_letters)
        data.pop(i)
    return res


def letter_difference(label_one, label_two):
    '''Return number of letters different, and the common letters.'''
    num_different = 0
    same_letters = ''
    for i, letter in enumerate(label_one):
        if letter != label_two[i]:
            num_different += 1
        else:
            same_letters += letter

    return num_different, same_letters


if __name__ == '__main__':
    label_data = get_aoc_data_for_challenge(__file__)

    checksum = checksum_generator(label_data)
    print(checksum)  # 454

    fabric_label_solutions = common_letters_in_correct_labels(label_data)
    print(fabric_label_solutions[0])  # lufjygedpvfbhftxiwnaorzmq
