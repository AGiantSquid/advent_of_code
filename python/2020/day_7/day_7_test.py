'''
Demonstrates that code works for day 7.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_7 import count_parent_possibilities

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.',
]


def test_count_parent_possibilities():
    res = count_parent_possibilities(data)
    assert res == 4


def test_count_parent_possibilities_pd():
    res = count_parent_possibilities(PUZZLE_DATA)
    assert res == 274
