import os
import requests

URL='https://adventofcode.com/2018/day/1/input'

# get my user-specific cookies
cookie_file = os.path.join(os.path.dirname(__file__), '../cookies.txt')
with open(cookie_file, 'r') as f:
  COOKIES=f.read()


def get_dataset_from_url(url, cookies, requests=requests):
    """Get request to url with cookies for user data."""
    resp = requests.get(
        url,
        cookies=dict(cookies_are=cookies)
    )
    # Filter empty results
    return filter(None, resp.text.split('\n'))


def get_end_frequency(frequency_changes):
    """Sum numbers together to get result frequency."""
    return sum(int(num) for num in frequency_changes)


if __name__ == '__main__':
    FREQUENCY_LIST = get_dataset_from_url(URL, COOKIES)
    END_FREQUENCY = get_end_frequency(FREQUENCY_LIST)
    print(END_FREQUENCY)  # 454
