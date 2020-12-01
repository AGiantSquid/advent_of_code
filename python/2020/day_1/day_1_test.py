from day_1 import find_2020_entries, get_product_of_entries, find_2020_entries_three, get_product_of_entries_three

NUMS = [
    '1721',
    '979',
    '366',
    '299',
    '675',
    '1456',
]


def test_find_2020_entries():
    entries = find_2020_entries(NUMS)
    assert 1721 in entries
    assert 299 in entries


def test_get_product_of_entries():
    res = get_product_of_entries(NUMS)
    assert res == 514579


def test_find_2020_entries_three():
    entries = find_2020_entries_three(NUMS)
    assert 979 in entries
    assert 366 in entries
    assert 675 in entries


def test_get_product_of_entries_three():
    res = get_product_of_entries_three(NUMS)
    assert res == 241861950
