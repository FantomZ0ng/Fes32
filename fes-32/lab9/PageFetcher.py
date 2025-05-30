import requests
from bs4 import BeautifulSoup


class PageFetcher:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    def fetch(self, url=None):
        try:
            response = requests.get(url or self.url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')

        except requests.exceptions.RequestException as e:
            print(f"Can't fetch: {e}")
