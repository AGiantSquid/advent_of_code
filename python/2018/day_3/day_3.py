#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 3.
'''

from aoc_utils import get_aoc_data_for_challenge


def get_id_x_y_w_h(data):
    '''Parse the id, x and y coords, and width and height from string.'''
    pattern_id, _, lr, dimensions = data.split(' ')
    x, y = [int(_) for _ in lr[:-1].split(',')]
    width, height = [int(_) for _ in dimensions.split('x')]

    return pattern_id, x, y, width, height


def get_dupes(data):
    '''Return duplicate coords.'''
    all_coords = set()
    dupes = set()
    for el in data:
        _, x, y, width, height = get_id_x_y_w_h(el)

        for i in range(x, x + width):
            for j in range(y, y + height):
                coord = (i, j)
                if coord in all_coords:
                    dupes.add(coord)
                else:
                    all_coords.add(coord)
    return dupes


def get_overlapping_fabric(data):
    '''Return count of overlapping coordinates in data.'''
    dupes = get_dupes(data)

    return len(dupes)


def get_non_overlapping_pattern_id(data):
    '''Return id of fabric pattern that is unique.'''
    dupes = get_dupes(data)

    for el in data:
        pattern_id, x, y, width, height = get_id_x_y_w_h(el)

        the_one = True
        for i in range(x, x + width):
            for j in range(y, y + height):
                coord = (i, j)
                if coord in dupes:
                    the_one = False

        if the_one:
            return pattern_id[1:]

    return None


if __name__ == '__main__':
    pattern_data = get_aoc_data_for_challenge(__file__)

    overlaps = get_overlapping_fabric(pattern_data)
    print(overlaps)  # 112418

    non_overlap_id = get_non_overlapping_pattern_id(pattern_data)
    print(non_overlap_id)  # 560
