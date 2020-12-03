#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 3.
'''

from aoc_utils import get_aoc_data_for_challenge


def get_overlapping_fabric(data):
    '''Return count of overlapping coordinates in data.'''
    all_coords = set()
    dupes = set()
    for el in data:
        id, at, lr, dimensions = el.split(' ')
        x, y = [int(_) for _ in lr[:-1].split(',')]
        width, height = [int(_) for _ in dimensions.split('x')]

        for i in range(x, x + width):
            for j in range(y, y + height):
                coord = (i, j)
                if coord in all_coords:
                    dupes.add(coord)
                else:
                    all_coords.add(coord)

    return len(dupes)


if __name__ == '__main__':
    data = get_aoc_data_for_challenge(__file__)

    overlaps = get_overlapping_fabric(data)
    print(overlaps)  # 112418
