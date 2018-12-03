import itertools
import os
import requests

URL='https://adventofcode.com/2018/day/1/input'

# get my user-specific cookies
cookie_file = os.path.join(os.path.dirname(__file__), '../cookies.txt')
with open(cookie_file, 'r') as f:
  COOKIES=f.read()


def get_dataset_from_url(url, cookies):
    """Get request to url with cookies for user data."""
    resp = requests.get(
        url,
        cookies=dict(cookies_are=COOKIES)
    )
    # Filter empty results
    return filter(None, resp.text.split('\n'))


def get_repeated_frequency(frequency_changes):
    """Returns first sum of cycled numbers that repeats."""
    frequency = 0
    found_frequencies = []
    for num in itertools.cycle(frequency_changes):
        frequency += int(num)
        if frequency in found_frequencies:
            return frequency
        found_frequencies.append(frequency)


if __name__ == '__main__':
    FREQUENCY_LIST = get_dataset_from_url(URL, COOKIES)
    END_FREQUENCY = get_repeated_frequency(FREQUENCY_LIST)

    print (END_FREQUENCY)  # 566
