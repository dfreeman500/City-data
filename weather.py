import requests
import api
location = "Miami"

# url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(location, api.openWeatherApi)
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(location, api.openWeatherApi))
# api.openweathermap.org/data/2.5/weather?q=London,uk&appid=233e46e5c3802b481c5caf4d659233c2

print(response.json()["main"]["temp"])

print(response.status_code)
