from collections import Counter

from day_2.day_2_test_data import EXPECTED_PAYLOAD
from aoc_utils import get_dataset_from_url


def common_letters_in_correct_labels(data):
  res = []
  for i, label in enumerate(data):
    for compare_label in data:
      one_letter_difference, same_letters = one_letter_different(label, compare_label)
      if one_letter_difference:
        res.append(same_letters)
    data.pop(i)
  return list(res)


def one_letter_different(label_one, label_two):
  num_different = 0
  same_letters = ''
  for i, letter in enumerate(label_one):
    if letter != label_two[i]:
      num_different += 1
    else:
      same_letters += letter

  return num_different == 1, same_letters


if __name__ == '__main__':
    URL='https://adventofcode.com/2018/day/2/input'

    LABEL_DATA = get_dataset_from_url(URL)
    FABRIC_LABEL_SOLUTIONS = common_letters_in_correct_labels(LABEL_DATA)

    # problem implies there is only one solution
    if len(FABRIC_LABEL_SOLUTIONS) == 1:
      print(FABRIC_LABEL_SOLUTIONS[0])  # lufjygedpvfbhftxiwnaorzmq
    else:
      print(FABRIC_LABEL_SOLUTIONS)
