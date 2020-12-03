from os.path import join, dirname, abspath

from aoc_utils import get_aoc_data_for_challenge
from day_2 import checksum_generator, common_letters_in_correct_labels


LABEL_DATA_PAYLOAD = get_aoc_data_for_challenge(__file__)


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
