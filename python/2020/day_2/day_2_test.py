from day_2 import password_checker_range, password_checker_index


data = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]


def test_password_checker_range():
    res = password_checker_range(data)
    assert res == 2


def test_password_checker_index():
    res = password_checker_index(data)
    assert res == 1
