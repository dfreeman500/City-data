import api
import requests

class CityInfo:
    def __init__(self, cityState, weather):
        self.cityState = cityState
        self.weather = weather

    def weatherInfo(self, cityState):
        print("The temperature in {} is {} degrees Fahrenheit but it feels like {}.".format(cityState, self.weather["main"]["temp"],self.weather["main"]["feels_like"] ))

