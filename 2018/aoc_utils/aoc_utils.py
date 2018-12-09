import os
import requests

# get my user-specific cookies
cookie_file = os.path.join(os.path.dirname(__file__), '../cookies.txt')
with open(cookie_file, 'r') as f:
  COOKIES = f.read()

def get_dataset_from_url(url, cookies=COOKIES, requests=requests):
    """Get request to url with cookies for user data."""
    resp = requests.get(
        url,
        cookies=dict(cookies_are=cookies)
    )
    # Filter empty results
    return filter(None, resp.text.split('\n'))
