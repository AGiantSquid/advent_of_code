from day_two_a import checksum_generator
from day_two_test_data import EXPECTED_PAYLOAD
from aoc_utils import get_dataset_from_url


class MockResponse:
  def __init__(self):
    self.text = EXPECTED_PAYLOAD


class MockRequests:
  """Mock class to make GET request."""
  def get(self, url, cookies):
    return MockResponse()

MOCK_REQUESTS = MockRequests()

LABEL_DATA_PAYLOAD = list(get_dataset_from_url('some url', 'some cookies', MOCK_REQUESTS))

def test_checksum_generator():
  label_data = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab",
  ]
  result = checksum_generator(label_data)
  assert result == 12


def test_checksum_generator_real_data():
  label_data = LABEL_DATA_PAYLOAD
  result = checksum_generator(label_data)
  assert result == 4712
