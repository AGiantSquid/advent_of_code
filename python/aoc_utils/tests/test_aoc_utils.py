#!/usr/bin/env python3
import pytest

from aoc_utils import get_dataset_from_url, get_input_url, chunk_aoc_data
from test_data import EXPECTED_PAYLOAD


class MockResponse:
    def __init__(self, expected_payload):
        self.text = expected_payload


class MockRequests:
    '''Mock class to make GET request.'''
    def get(self, url, cookies):
        return MockResponse(EXPECTED_PAYLOAD)


MOCK_REQUESTS = MockRequests()


EXPECTED_FREQUENCY_LIST = '''-5
-2
+1
+14
+7'''


def test_get_dataset_from_url():
    """Tests get request to url with cookies for user data."""
    result = get_dataset_from_url('some url', 'some cookies', MOCK_REQUESTS)
    assert result == EXPECTED_FREQUENCY_LIST


def test_get_input_url():
    year = '2018'
    day = '12'
    res = get_input_url(year, day)
    assert res == 'https://adventofcode.com/2018/day/12/input'


def test_chunk_aoc_data():
    aoc_data = [
        'first',
        'group',
        'here',
        '',
        'new',
        'group',
        '',
        'last',
        'group',
        'of',
        'words',
    ]

    expected = (
        ('first', 'group', 'here'),
        ('new', 'group'),
        ('last', 'group', 'of', 'words'),
    )
    chunked = chunk_aoc_data(aoc_data)
    assert chunked == expected


def test_chunk_aoc_data_2():
    aoc_data = [
        'first',
        'group',
        'here',
        '##',
        'new',
        'group',
        '##',
        'last',
        'group',
        'of',
        '',
        'words',
    ]

    expected = (
        ('first', 'group', 'here'),
        ('new', 'group'),
        ('last', 'group', 'of', '', 'words'),
    )
    chunked = chunk_aoc_data(aoc_data, separator='##')
    assert chunked == expected


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
