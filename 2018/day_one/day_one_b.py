import itertools

from aoc_utils import get_dataset_from_url


def get_repeated_frequency(frequency_changes):
    """Returns first sum of cycled numbers that repeats."""
    frequency = 0
    found_frequencies = []
    for num in itertools.cycle(frequency_changes):
        frequency += int(num)
        if frequency in found_frequencies:
            return frequency
        found_frequencies.append(frequency)


if __name__ == '__main__':
    URL='https://adventofcode.com/2018/day/1/input'

    FREQUENCY_LIST = get_dataset_from_url(URL)
    END_FREQUENCY = get_repeated_frequency(FREQUENCY_LIST)

    print(END_FREQUENCY)  # 566
