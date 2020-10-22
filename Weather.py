import api
import requests

def getWeather(cityState):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(cityState, api.openWeatherApi))
    return [ response.status_code, cityState, response.json()]

