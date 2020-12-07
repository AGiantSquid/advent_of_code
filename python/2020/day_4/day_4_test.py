from aoc_utils import get_aoc_data_for_challenge
from day_4 import valid_passport_count, range_validator, valid_height, valid_hair, valid_eye, valid_pid, valid_passport, valid_passport_2


PUZZLE_DATA = get_aoc_data_for_challenge(__file__, filter_nulls=False)

data = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]


def test_valid_passport_count():
    res = valid_passport_count(data, valid_passport)
    assert res == 2


def test_valid_passport_count_puzzle_data():
    res = valid_passport_count(PUZZLE_DATA, valid_passport)
    assert res == 219


def test_validators():
    rv = range_validator(1920, 2002)
    assert rv('2002') is True
    assert rv('2003') is False

    assert valid_height('150cm') is True
    assert valid_height('149cm') is False
    assert valid_height('76in') is True

    assert valid_hair('#fa0088') is True
    assert valid_hair('#ha0088') is False
    assert valid_hair('#aa0088a') is False

    assert valid_eye('amb') is True
    assert valid_eye('aoeu') is False

    assert valid_pid('000123456') is True
    assert valid_pid('00012345a') is False
    assert valid_pid('a00123456') is False
    assert valid_pid('a001234560') is False


def test_valid_passport_count_2():
    res = valid_passport_count(data, valid_passport_2)
    assert res == 2


def test_valid_passport_count_2_puzzle_data():
    res = valid_passport_count(PUZZLE_DATA, valid_passport_2)
    assert res == 127
