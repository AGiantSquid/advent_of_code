#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 4.
'''
from typing import Collection


from collections import Counter
from aoc_utils import get_aoc_data_for_challenge


def split_on_nth_char(source, n, char):
    divided = source.split(char, n)
    return char.join(divided[:n]), divided[n]


def get_guard_dict(data):
    new_data = [split_on_nth_char(el, 2, ' ') for el in data]

    sorted_data = sorted(new_data, key=lambda x: x[0])

    guard_dict = {}

    curr_guard = None
    for el in sorted_data:
        if el[1].startswith('Guard'):
            guard_num = el[1].split(' ')[1]
            curr_guard = guard_num
            guard_dict[curr_guard] = guard_dict.get(
                curr_guard,
                {'sleep_mins': [], 'last_sleep_time': None, 'total': 0},
            )
            continue

        time = int(el[0][15:17])

        if el[1].startswith('falls'):
            guard_dict[curr_guard]['last_sleep_time'] = time
        if el[1].startswith('wakes'):
            for i in range(guard_dict[curr_guard]['last_sleep_time'], time):
                guard_dict[curr_guard]['sleep_mins'].append(i)
                guard_dict[curr_guard]['total'] += 1

    return guard_dict


def get_product_of_guard_id_and_minute(data):
    '''Find the guard most likely to sleep and multiply their id by the minute they sleep the most.'''
    guard_dict = get_guard_dict(data)

    max_sleeper = max(guard_dict, key=lambda x: guard_dict[x]['total'])
    c = Counter(guard_dict[max_sleeper]['sleep_mins'])
    most_common_minute = max(c, key=lambda x: c[x])

    return int(max_sleeper[1:]) * most_common_minute


def get_product_of_guard_id_and_minute_2(data):
    '''Find the guard most likely to sleep and multiply their id by the minute they sleep the most.'''
    guard_dict = get_guard_dict(data)

    for k, v in guard_dict.items():
        c = Counter(v['sleep_mins'])
        if c:
            max_min = max(c, key=lambda x: c[x])
            guard_dict[k]['max_min'] = [c[max_min], max_min]
        else:
            guard_dict[k]['max_min'] = [0, 0]

    max_minute_holder = max(guard_dict, key=lambda x: guard_dict[x]['max_min'][0])

    return int(max_minute_holder[1:]) * guard_dict[max_minute_holder]['max_min'][1]


if __name__ == '__main__':
    data = get_aoc_data_for_challenge(__file__)

    overlaps = get_product_of_guard_id_and_minute(data)
    print(overlaps)  # 36898

    max_minute_sleeper = get_product_of_guard_id_and_minute_2(data)
    print(max_minute_sleeper)  # 36898
