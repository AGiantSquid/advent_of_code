import pytest

from aoc_utils import get_dataset_from_url
from test_data import EXPECTED_PAYLOAD


class MockResponse:
  def __init__(self, expected_payload):
    self.text = expected_payload


class MockRequests:
  """Mock class to make GET request."""
  def get(self, url, cookies):
    return MockResponse(EXPECTED_PAYLOAD)


MOCK_REQUESTS = MockRequests()


EXPECTED_FREQUENCY_LIST = ['-5', '-2', '+1', '+14', '+7']


def test_get_dataset_from_url():
    """Tests get request to url with cookies for user data."""
    result = list(get_dataset_from_url('some url', 'some cookies', MOCK_REQUESTS))
    assert result == EXPECTED_FREQUENCY_LIST


if __name__ == '__main__':
  import sys
  pytest.main(sys.argv)
