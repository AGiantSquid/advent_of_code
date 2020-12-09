#!/usr/bin/env python3
'''
Solves Advent of Code problem for day 8.
'''

from typing import List

from aoc_utils import get_aoc_data_for_challenge


def get_total_at_repeat(data: List[str]):
    # 'acc', 'jmp', or 'nop'
    run_instructions = set()
    accum = 0
    new_data = [_.split(' ') for _ in data]

    return perform_instruction(new_data, run_instructions, accum, 0)


def perform_instruction(data, run_instructions, accum, i):
    if i in run_instructions:
        return accum
    run_instructions.add(i)

    typ, diff = data[i]

    if typ == 'jmp':
        return perform_instruction(data, run_instructions, accum, i + int(diff))
    if typ == 'acc':
        accum += int(diff)

    return perform_instruction(data, run_instructions, accum, i + 1)


def get_total(data: List[str]):
    # 'acc', 'jmp', or 'nop'
    new_data = [_.split(' ') for _ in data]
    processed = [[_[0], int(_[1])] for _ in new_data]

    for mutation in generate_mutations(processed):
        res = perform_instruction_2(mutation, set(), 0, 0)
        if res:
            return res


def generate_mutations(data):
    def mutate(el):
        typ, diff = el
        if typ == 'jmp':
            return ['nop', diff]
        if typ == 'nop':
            return ['jmp', diff]
        return None

    for i, el in enumerate(data):
        new = mutate(el)
        if not new:
            continue
        yield data[:i] + [new] + data[i + 1:]


def perform_instruction_2(data, run_instructions, accum, i):
    if i in run_instructions:
        return None
    if i >= len(data):
        return accum
    run_instructions.add(i)

    typ, diff = data[i]

    if typ == 'jmp':
        return perform_instruction_2(data, run_instructions, accum, i + diff)
    if typ == 'acc':
        accum += diff

    return perform_instruction_2(data, run_instructions, accum, i + 1)



if __name__ == '__main__':
    puzzle_data = get_aoc_data_for_challenge(__file__, filter_nulls=False)

    result = get_total_at_repeat(puzzle_data)
    print(result)  # 1487

    result = get_total(puzzle_data)
    print(result)  # 1607
