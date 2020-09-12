from day_2_a import checksum_generator
from day_2_b import common_letters_in_correct_labels
from day_2_test_data import EXPECTED_PAYLOAD
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


def test_common_letters_in_correct_labels():
  label_data = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz",
  ]
  expected_result = 'fgij'
  results = common_letters_in_correct_labels(label_data)
  assert results[0] == expected_result


def test_common_letters_in_correct_labels_real_data():
  label_data = LABEL_DATA_PAYLOAD
  results = common_letters_in_correct_labels(label_data)
  assert results[0] == 'lufjygedpvfbhftxiwnaorzmq'
