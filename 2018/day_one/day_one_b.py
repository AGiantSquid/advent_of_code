import requests
import itertools

URL='https://adventofcode.com/2018/day/1/input'
COOKIES='_ga=GA1.2.1115296876.1543798028; _gid=GA1.2.2143035274.1543798028; session=53616c7465645f5f6b955b505a9a6b80358b71e3a89e1ec85fee9078ee71ad34d8eb7425b17a184d1d9ba97ae8224288'


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
