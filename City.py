import api
import requests

class CityInfo:
    def __init__(self, cityState):
        self.cityState = cityState
        self.response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(self.cityState, api.openWeatherApi))

    
    def printCity(self, cityState):
        print("You wish to learn more about", cityState)


   
    def temperature(self, cityState):
        print("The temperature in {} is {} degrees Farenheit.".format(cityState, self.response.json()["main"]["temp"]))
        print(self.response.status_code)

