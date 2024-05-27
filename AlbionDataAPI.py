from requests import get, exceptions


class AlbionDataAPI:
    def __init__(self, resource, tier, enchant):
        self.API_URL = 'https://europe.albion-online-data.com/api/v2/stats'
        self.LOCATIONS = 'locations=Lymhurst,Bridgewatch,Fort Sterling,Martlock,Thetford,Caerleon,Brecilien'

        self.resource = resource[0]
        self.tier = tier[0]
        self.enchant = enchant[0]

    def get_resource_prices(self):
        item = f'{self.tier}_{self.resource}_{self.enchant}' if self.enchant != '0' else f'{self.tier}_{self.resource}'
        url = f'{self.API_URL}/prices/{item}/?{self.LOCATIONS}'

        try:
            response = get(url)
            response.raise_for_status()
            data = response.json()
            return data

        except exceptions.HTTPError as http_err:
            if response.status_code == 404:
                message = f"Nie znaleziono zasobu {self.resource} T{self.tier}.{self.enchant}."
            else:
                message = f"Wystąpił błąd HTTP: {http_err}"
            return {'error': message}

        except Exception as error:
            return {'error': f'Wystąpił problem {error}'}


