'''
Utility functions to help with Advent of Code.
'''
import requests as requests_module


def get_dataset_from_url(url, cookies, requests=requests_module):
    '''Get request to url with cookies for user data.'''
    resp = requests.get(
        url,
        cookies=dict(cookies_are=cookies)
    )
    # Filter empty results
    return filter(None, resp.text.split('\n'))


def read_cookies_from_file(cookie_file: str):
    '''Read cookies from file and format.'''
    with open(cookie_file, 'r') as f:
        cookies = f.read().strip()
    return cookies
