import api
import requests

def getWeather(cityState):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(cityState, api.openWeatherApi))
    # print(response.status_code)
    # print(response.json())
    # if response.status_code == 200:
    return [ response.status_code, cityState, response.json()]
    # else:
    #     return [ response.status_code, cityState, "try again" ]
