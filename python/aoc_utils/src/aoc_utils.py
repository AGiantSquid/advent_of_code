'''
Utility functions to help with Advent of Code.
'''
from os.path import join, dirname, basename, isfile
from string import Template

import requests as requests_module


ADVENT_URL = Template('https://adventofcode.com/$year/day/$day/input')
FILE_SAVED_EARLY_MSG = "Please don't repeatedly request this endpoint before it unlocks!"


def get_aoc_data_for_challenge(target_file, filter_nulls=True):
    '''Get data from aoc website, cache it locally, and return it.

    Use the path of the source project file to determine the day and year
    of the target challenge. Call out to aoc backend, and save the result
    to a file "data.txt". Return the resulting data as a list.
    '''
    day_project_file = dirname(target_file)
    year_project_file = dirname(day_project_file)

    data_file_path = join(day_project_file, 'data.txt')

    # check if file exists already
    if isfile(data_file_path):
        data = get_data_from_file(data_file_path)
        if not data.startswith(FILE_SAVED_EARLY_MSG):
            return get_data_list(data, filter_nulls)

    year = basename(year_project_file)
    day = basename(day_project_file).split('_')[1]

    url = get_input_url(year, day)

    cookie_file = join(year_project_file, 'cookies.txt')
    cookies = get_data_from_file(cookie_file)

    data = get_dataset_from_url(url, cookies)

    if data.startswith(FILE_SAVED_EARLY_MSG):
        print('Its too early to get the puzzle data!')
        return

    with open(data_file_path, 'w') as f:
        f.write(data)

    return get_data_list(data, filter_nulls)


def get_data_from_file(file_path: str) -> str:
    '''Read data from file and return.'''
    with open(file_path, 'r') as f:
        data = f.read().rstrip()
    return data


def get_data_list(data, filter_nulls=True):
    '''Split data on newlines, and return non-Null values.'''
    split_data = data.split('\n')

    if not filter_nulls:
        return list(split_data)

    return list(filter(None, data.split('\n')))



def get_input_url(year: str, day: str) -> str:
    '''Interpolate year and day into url.'''
    url = ADVENT_URL.substitute(year=year, day=day)
    return url


def get_dataset_from_url(url, cookies, requests=requests_module):
    '''Get request to url with cookies for user data.'''
    print('Getting data from Advent of Code')
    resp = requests.get(
        url,
        cookies=dict(cookies_are=cookies)
    )

    return resp.text.rstrip()
