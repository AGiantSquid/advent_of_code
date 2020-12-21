#!/usr/bin/env python3
'''
Create a module for a Advent of Code challenge.
'''
import os
import sys
from string import Template


FILE_TEMPLATE = Template("""\
#!/usr/bin/env python3
'''
Solves Advent of Code problem for day $day_number.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def part_1(data: List[str]):
    pass


def part_2(data: List[str]):
    pass


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    puzzle_data = [

    ]

    result = part_1(puzzle_data)
    print(result)

    # result = part_2(puzzle_data)
    # print(result)
""")

TEST_FILE_TEMPLATE = Template("""\
'''
Demonstrates that code works for day $day_number.
'''
import pytest

from aoc_utils import get_aoc_data_for_challenge
from day_$day_number import part_1, part_2

PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

DATA = [

]


def test_part_1():
    res = part_1(DATA)
    assert res == 0


# def test_part_1_pd():
#     res = part_1(PUZZLE_DATA)
#     assert res == 0


# def test_part_2():
#     res = part_2(DATA)
#     assert res == 0


# def test_part_2_pd():
#     res = part_2(PUZZLE_DATA)
#     assert res == 0


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
""")


if __name__ == '__main__':
    try:
        puzzle_year = sys.argv[1]
    except IndexError:
        puzzle_year = input('Enter year number:\n')

    try:
        puzzle_day = sys.argv[2]
    except IndexError:
        puzzle_day = input('Enter day number:\n')

    year_num = int(puzzle_year)
    day_num = int(puzzle_day)

    project_dir = os.path.dirname(os.path.abspath(__file__))

    target_dir = os.path.join(project_dir, puzzle_year, f'day_{day_num}')
    os.mkdir(target_dir)

    main_file = os.path.join(target_dir, f'day_{day_num}.py')
    with open(main_file, 'w') as f:
        f.write(FILE_TEMPLATE.substitute(day_number=day_num))

    test_file = os.path.join(target_dir, f'day_{day_num}_test.py')
    with open(test_file, 'w') as f:
        f.write(TEST_FILE_TEMPLATE.substitute(day_number=day_num))

    print(f'run:\n\npython {os.path.relpath(main_file)}\n')
    print(f'test:\n\npytest {os.path.relpath(target_dir)} -s\n')
