#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 7.
'''

from typing import List, Tuple

from aoc_utils import get_aoc_data_for_challenge


BAG_COLOR = 'shiny gold'


def count_parent_possibilities(data: List[str]) -> int:
    bd = get_bag_dict(data)

    return len(get_parents(bd, BAG_COLOR, set()))


def get_parents(bag_dict, start, parents):
    v = bag_dict.get(start, [])

    if v:
        for _ in v:
            parents.add(_)
            parents = get_parents(bag_dict, _, parents)

    return parents


def get_bag_dict(data: List[str]) -> dict:
    d = {}

    for rule in data:
        key = clean_label(rule.split('contain')[0])
        rest = [clean_label(_) for _ in rule.split('contain')[1].split(', ')]
        d[key] = rest

    inversed = {}

    for k, v in d.items():
        for i in v:
            inversed[i] = inversed.get(i, []) + [k]

    return inversed


def clean_label(label: str) -> str:
    no_bag = label.split('bag')[0].strip()
    no_num = ' '.join(no_bag.split(' ')[-2:])
    return no_num


def count_children(data: List[str]) -> int:
    bd = get_bag_dict_2(data)
    return get_children(bd, BAG_COLOR, 0)


def get_children(bag_dict, start, children):
    v = bag_dict.get(start, [])

    if v:
        for _ in v:
            if _:
                for i in range(_[1]):
                    children += 1
                    children = get_children(bag_dict, _[0], children)

    return children


def get_bag_dict_2(data: List[str]) -> dict:
    d = {}

    for rule in data:
        key = clean_label(rule.split('contain')[0])
        rest = [clean_label_2(_) for _ in rule.split('contain')[1].split(', ')]
        d[key] = rest

    return d


def clean_label_2(label: str) -> Tuple[str, int]:
    no_bag = label.split('bag')[0].strip()
    if no_bag.startswith('no other'):
        return None

    num, no_num = no_bag.split(' ', 1)
    return no_num, int(num)


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = count_parent_possibilities(puzzle_data)
    print(result)  # 274

    result = count_children(puzzle_data)
    print(result)  # 274
