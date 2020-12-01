from day_1 import find_2020_entries, get_product_of_entries

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
