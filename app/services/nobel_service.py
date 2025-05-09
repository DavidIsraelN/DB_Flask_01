from repositories.nobel_repository import NobelRepository


class NobelService:
    def get_country_code(self, country):
        """
        Get the country code for a given country name.
        :param country: The name of the country.
        :return: The country code if found, otherwise None.
        """
        try:
            data = NobelRepository().fetch_country_data()
            for item in data.get('countries', []):
                if item.get('name').lower() == country.lower():
                    return item.get('code')
            raise ValueError(f"Country code not found for {country}")
        
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error fetching country code: {str(e)}")
