#!/usr/bin/env python3
import itertools

from aoc_utils import get_aoc_data_for_challenge


def get_end_frequency(frequency_changes):
    '''Sum numbers together to get result frequency.'''
    return sum(int(num) for num in frequency_changes)


def get_repeated_frequency(frequency_changes):
    '''Returns first sum of cycled numbers that repeats.'''
    frequency = 0
    found_frequencies = set()
    frequency_changes_ints = [int(_) for _ in frequency_changes]

    for num in itertools.cycle(frequency_changes_ints):
        frequency += num
        if frequency in found_frequencies:
            return frequency
        found_frequencies.add(frequency)


if __name__ == '__main__':
    frequency_list = get_aoc_data_for_challenge(__file__)

    end_frequency = get_end_frequency(frequency_list)
    print(end_frequency)  # 454

    repeated_frequency = get_repeated_frequency(frequency_list)
    print(repeated_frequency)  # 566
