import pprint
import requests

url = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&APPID=" \
      "49467897723d2f8b344ab7e15e10737f&units=imperial"

url = "https://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.4&APPID=" \
      "49467897723d2f8b344ab7e15e10737f&units=imperial"


class Weather:
    """
    Create a weather object getting the apikey as the input
    and either the city name or the lat and long coordinate.
    Package use example:
    Create the weather object using the city name:
    The API key is not guaranteed to work.
    Get your own Apikey from the https://openweathermap.org
    And wait for a couple of hours for the apikey to be activated.

    weather2=Weather(apikey='49467897723d2f8b344ab7e15e10737f' lat=4.1, lon=3.2)

    Get the complete weather data for the next 12 hours
    weather2.next_12h()

    Simplified Data for the next 12 hours:
    weather2.next12h_simplified()

    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        # Using the if else condition:
        # If both the city and the lat & lon provided, the city block
        # will be executed
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            # The self keyword is referencing to the weather object, weather.data
            # it is converted into dictionary using the .json()
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            # User did not provide anything, Hence, it is a TypeError
            raise TypeError("Provide either city or Lat and Lon Argument")
        if self.data['cod'] != '200':
            # User pass the wrong value, hence it is a ValueError.
            raise ValueError(self.data["message"])

    @property
    def next_12h(self):
        """Each data is only 3 hours, hence, you will need 4 data which is from [:4],
        This will return 3 hours for next 12 hours as a dict"""
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ Return data, temperature, and the sky condition every 3hours
        for the next 12hours as the tuple of tuples"""
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'],
                                dicty['weather'][0]['description']))
        return simple_data


# Instantiate the weather object
weather = Weather(apikey='49467897723d2f8b344ab7e15e10737f', city='Malaysia')

pprint.pprint(weather.next_12h_simplified())
