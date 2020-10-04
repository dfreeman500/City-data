from City import CityInfo
# import os
import time
from Weather import getWeather
cityList = [] #keeps track of userinput/cities for history or comparison purposes

print("""
        Welcome to the City-data app. Find out information about a city (ex: Louisville, Kentucky)
        

""")


def chooseCity(menuChoice):
    responses = getWeather(menuChoice)
    return responses  #returns [ response.status_code, cityState, response.json()]





while True:
    # os.system('cls||clear')


    menuChoice = input("""


    
        1.) Enter a city, state to find out information about it
            or 
        2.) Type 'exit' to exit

        """)

    if menuChoice.lower() == "exit":
        break
    
    else:
        cityData = chooseCity(menuChoice)
        # print(cityData[0])
        if cityData[0] != 200:
            print("You entered {} but that wasn't found. Please try again. Please use the format of 'Louisville, Kentucky'".format(cityData[1]))

        else:
            b = CityInfo(cityState = cityData[1], weather = cityData[2]) ## creates an instance of CityInfo class passing in the cityRequest
            b.weatherInfo(cityState = cityData[1])


