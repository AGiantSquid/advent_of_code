from aoc_utils import get_aoc_data_for_challenge
from day_3 import get_trees_hit_part_1, get_trees_hit_part_2


PUZZLE_DATA = get_aoc_data_for_challenge(__file__)

data = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]

def test_get_trees_hit_part_1():
    res = get_trees_hit_part_1(data)
    assert res == 7


def test_get_trees_hit_part_1_puzzle_data():
    res = get_trees_hit_part_1(PUZZLE_DATA)
    assert res == 276


def test_get_trees_hit_part_2():
    res = get_trees_hit_part_2(data)
    assert res == 336


def test_get_trees_hit_part_2_puzzle_data():
    res = get_trees_hit_part_2(PUZZLE_DATA)
    assert res == 7812180000
