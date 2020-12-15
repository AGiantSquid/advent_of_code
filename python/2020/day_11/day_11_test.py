'''
Demonstrates that code works for day 11.
'''
from aoc_utils import get_aoc_data_for_challenge
from day_11 import draw_new_map, part_1, part_2, check_for_occupied_in_sight, draw_new_map_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

DATA = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL',
]


def test_draw_new_map():
    res = draw_new_map(DATA)

    expected = [
        '#.##.##.##',
        '#######.##',
        '#.#.#..#..',
        '####.##.##',
        '#.##.##.##',
        '#.#####.##',
        '..#.#.....',
        '##########',
        '#.######.#',
        '#.#####.##',
    ]

    assert res == expected

    res2 = draw_new_map(expected)

    expected2 = [
        '#.LL.L#.##',
        '#LLLLLL.L#',
        'L.L.L..L..',
        '#LLL.LL.L#',
        '#.LL.LL.LL',
        '#.LLLL#.##',
        '..L.L.....',
        '#LLLLLLLL#',
        '#.LLLLLL.L',
        '#.#LLLL.##',
    ]

    assert res2 == expected2

    res3 = draw_new_map(expected2)

    expected3 = [
        '#.##.L#.##',
        '#L###LL.L#',
        'L.#.#..#..',
        '#L##.##.L#',
        '#.##.LL.LL',
        '#.###L#.##',
        '..#.#.....',
        '#L######L#',
        '#.LL###L.L',
        '#.#L###.##',
    ]

    assert res3 == expected3


def test_part_1():
    res = part_1(DATA)
    assert res == 37


def test_draw_new_map_pd():
    res = part_1(PUZZLE_DATA)
    assert res == 2299


def test_check_for_occupied_in_sight():
    data = [
        '.......#.',
        '...#.....',
        '.#.......',
        '.........',
        '..#L....#',
        '....#....',
        '.........',
        '#........',
        '...#.....',
    ]
    res = check_for_occupied_in_sight(data, 4, 3)
    assert res == 8


def test_check_for_occupied_in_sight_2():
    data = [
        '.............',
        '.L.L.#.#.#.#.',
        '.............',
    ]
    res = check_for_occupied_in_sight(data, 1, 1)
    assert res == 0


def test_check_for_occupied_in_sight_3():
    data = [
        '.##.##.',
        '#.#.#.#',
        '##...##',
        '...L...',
        '##...##',
        '#.#.#.#',
        '.##.##.',
    ]
    res = check_for_occupied_in_sight(data, 3, 3)
    assert res == 0


def test_check_for_occupied_in_sight_4():
    data = [
        '#.LL.LL.L#',
        '#LLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLL#',
        '#.LLLLLL.L',
        '#.LLLLL.L#',
    ]
    res = check_for_occupied_in_sight(data, 1, 0)
    assert res == 1
    res = check_for_occupied_in_sight(data, 0, 3)
    assert res == 0


def test_draw_new_map_2():
    step1 = draw_new_map_2(DATA)

    expected = [
        '#.##.##.##',
        '#######.##',
        '#.#.#..#..',
        '####.##.##',
        '#.##.##.##',
        '#.#####.##',
        '..#.#.....',
        '##########',
        '#.######.#',
        '#.#####.##',
    ]

    assert step1 == expected
    step2 = draw_new_map_2(step1)

    expected = [
        '#.LL.LL.L#',
        '#LLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLL#',
        '#.LLLLLL.L',
        '#.LLLLL.L#',
    ]

    assert step2 == expected

    step3 = draw_new_map_2(step2)

    expected = [
        '#.L#.##.L#',
        '#L#####.LL',
        'L.#.#..#..',
        '##L#.##.##',
        '#.##.#L.##',
        '#.#####.#L',
        '..#.#.....',
        'LLL####LL#',
        '#.L#####.L',
        '#.L####.L#',
    ]

    assert step3 == expected


def test_part_2():
    res = part_2(DATA)
    assert res == 26


def test_part_2_pd():
    res = part_2(PUZZLE_DATA)
    assert res == 2047
