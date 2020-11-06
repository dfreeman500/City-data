from city import CityInfo
import time
from weather import getWeather
from wiki import GetWiki
import csv_export
import graph_data
import order

# firstRun and runMode are for csv exporter so header is only exported the first time
firstRun = True 
runMode = 'w'

cityList = [] #keeps track of cities that have been stored into the csv file

print("""
        Welcome to the City-data app. Find out information about a city (ex: Lexington, Kentucky)
        

""")

while True:
    if len(cityList)>0:
        graphOption = """  
        2.) Type '2' to see a history of cities that have been loaded into the csv.
            or
        3.) Type '3' to see a graph of estimated populations (some cities on wikipedia do not show estimated population).
            or
        4.) Type '4' to see a graph of population density for the different cities.
            or
        """
    else:
        graphOption = ''

    menuChoice = input("""


    
        1.) Enter a city, state (ex: 'Louisville, Kentucky') to find out information about it
            or {}
        
            Type 'exit' to exit

        

        """.format(graphOption))

    if menuChoice.lower() == "exit" or menuChoice.lower()=="e":
        break

    if menuChoice == '2' and len(cityList)>0:
        print("Number of cities with data in the csv file: {}".format(len(cityList)))
        for city in enumerate(cityList, start = 1):
            print(city)
        continue

    if menuChoice =='3' and len(cityList)>0:
        graph_data.graphPop()
        continue

    if menuChoice =='4' and len(cityList)>0:
        graph_data.graphPopDensity()
        continue

    else:
        firstRun, runMode, menuChoice, cityList = order.orderOfOps(firstRun,runMode, menuChoice, cityList, requestor="main")
        

        