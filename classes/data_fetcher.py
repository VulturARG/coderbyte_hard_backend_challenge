from requests import get


class DataFetcher:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = get(self.url)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()
