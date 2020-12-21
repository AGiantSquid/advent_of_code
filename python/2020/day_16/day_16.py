#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 16.
'''
from itertools import chain
from typing import List
from math import prod

from aoc_utils import get_aoc_data_for_challenge, chunk_aoc_data
from python_utils.sequence_utils import unpack_apply


def part_1(data: List[str]):
    chunked = chunk_aoc_data(data)
    valid_ranges, _, nearby_ticket_vals = unpack_apply(chunked, get_valid_ranges, None, get_nearby_ticket_values)

    collapsed_ranges = collapse_valid_ranges(chain.from_iterable(valid_ranges.values()))
    flattened_tickets = chain.from_iterable(nearby_ticket_vals)

    return sum(get_invalid_numbers(collapsed_ranges, flattened_tickets))


def get_valid_ranges(x: str) -> dict:
    ranges = {
        k: v
        for k, v in [unpack_apply(_.split(': '), None, clean_ranges) for _ in x]
    }
    return ranges


def clean_ranges(x):
    return [[int(s) for s in r.split('-')] for r in x.split(' or ')]


def collapse_valid_ranges(r):
    v = []
    s = sorted(r)
    for el in s:
        new = el[:]
        if not v:
            v.append(new)
            continue
        if new[0] > v[-1][1] + 1:
            v.append(new)
            continue
        if new[1] < v[-1][1]:
            continue
        v[-1][1] = new[1]

    return v


def get_invalid_numbers(valid_ranges, nearby_ticket_vals):
    invalid_numbers = []
    for val in nearby_ticket_vals:
        invalid = True
        for low, high in valid_ranges:
            if low <= val <= high:
                invalid = False
        if invalid:
            invalid_numbers.append(val)
    return invalid_numbers


def get_nearby_ticket_values(x):
    return [[int(n) for n in _.split(',')] for _ in x[1:]]


def part_2(data: List[str]):
    chunked = chunk_aoc_data(data)
    valid_ranges, ticket, nearby_ticket_vals = unpack_apply(
        chunked,
        get_valid_ranges,
        lambda x: [int(_) for _ in x[1].split(',')],
        get_nearby_ticket_values,
    )

    collapsed_ranges = collapse_valid_ranges(chain.from_iterable(valid_ranges.values()))
    flattened_tickets = chain.from_iterable(nearby_ticket_vals)

    invalid_numbers = set(get_invalid_numbers(collapsed_ranges, flattened_tickets))

    nearby_ticket_vals = nearby_ticket_vals + [ticket]
    valid_tickets = sorted(filter(lambda x: not len([_ for _ in x if _ in invalid_numbers]), nearby_ticket_vals), reverse=True)

    prop_map = get_prop_map(valid_ranges, valid_tickets)

    departure_vals = []
    for k, v in prop_map.items():
        if k.startswith('departure'):
            departure_vals.append(v)

    return prod([ticket[_] for _ in departure_vals])


def get_prop_map(valid_ranges, valid_tickets):
    possibilities = {}
    for prop, ranges in valid_ranges.items():
        for i in range(len(valid_tickets[0])):
            valid = True
            for vt in valid_tickets:
                inrange = ranges[0][0] <= vt[i] <= ranges[0][1] or ranges[1][0] <= vt[i] <= ranges[1][1]
                if not inrange:
                    valid = False
                    break
            if valid == True:
                possibilities[prop] = possibilities.get(prop, []) + [i]

    prop_map = {}
    while possibilities:
        for k, v in possibilities.items():
            if len(v) == 1:
                prop_map[k] = v[0]
                possibilities = {
                    key: [_ for _ in val if _ != v[0]]
                    for key, val in possibilities.items()
                    if key != k
                }

    return prop_map


if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = part_1(puzzle_data)
    print(result)

    result_2 = part_2(puzzle_data)
    print(result_2)
