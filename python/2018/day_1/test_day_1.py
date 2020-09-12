import pytest

from day_1_a import get_dataset_from_url, get_end_frequency
from day_1_b import get_repeated_frequency
from day_1_test_data import EXPECTED_PAYLOAD
from test_aoc_utils import MockResponse

class MockRequests:
  """Mock class to make GET request."""
  def get(self, url, cookies):
    return MockResponse(EXPECTED_PAYLOAD)

EXPECTED_FREQUENCY_LIST = get_dataset_from_url('some url', 'some cookies', MockRequests())


def test_get_end_frequency():
    """Sum numbers together to get result frequency."""
    frequency_changes = ["+1", "-2", "+3", "+1"]
    result = get_end_frequency(frequency_changes)
    assert result == 3


def test_get_end_frequency_real_data():
    frequency_changes = EXPECTED_FREQUENCY_LIST
    result = get_end_frequency(frequency_changes)
    assert result == 454


def test_get_repeated_frequency_example_1():
    frequency_changes = ["+1", "-2", "+3", "+1"]
    result = get_repeated_frequency(frequency_changes)
    assert result == 2


def test_get_repeated_frequency_example_2():
    frequency_changes = ["+3", "+3", "+4", "-2", "-4",]
    result = get_repeated_frequency(frequency_changes)
    assert result == 10


@pytest.mark.slow
def test_get_repeated_frequency_real_data():
    result = get_repeated_frequency(EXPECTED_FREQUENCY_LIST)
    assert result == 566


if __name__ == '__main__':
  import sys
  pytest.main(sys.argv)
