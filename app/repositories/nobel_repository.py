import requests
from config.config import URL_COUNTRY


class NobelRepository:
    def fetch_data(self, url):
        """
        Fetches data from the given URL.
        Raises an HTTPError for bad responses (4xx and 5xx).
        Returns the JSON response.
        """
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


    def fetch_country_data(self):
        return self.fetch_data(URL_COUNTRY)
