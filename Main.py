from City import CityInfo
# import os
import time

cityList = [] #keeps track of userinput/cities for history or comparison purposes

print("""
        Welcome to the City-data app. Find out information about a city (ex: Louisville, KY)
        

""")


def chooseCity():
    cityRequest = input("Enter city, state (ex: Louisville, KY) or 'exit': ")
    if cityRequest == "":
        print("please enter in city, state format (ex: Louisville, KY)")
        chooseCity()
    return cityRequest

city = chooseCity()
b = CityInfo(city)
while True:
    # os.system('cls||clear')

    menuChoice = input("""
        You have chosen: {}
        1.) Type 1 to learn about another city, state
        2.) Type 2 see the Current Temperature in {}
        3.) Type 3 to see all of the data for {}      
            or 
        Type "exit" to exit

        """.format(city, city, city))

    if menuChoice == "1":
        city = chooseCity()
        b = CityInfo(city)

    if menuChoice == "2" :
        b.temperature(city)
    if menuChoice == "3":
        print("Show all")

    if menuChoice.lower() == "exit":
        break




    

    




