from City import CityInfo
# import os
import time
from Weather import getWeather
from wiki import getWiki
import csv_export
import graph_data

# firstRun and runMode are for csv exporter so header only is exported the first time
firstRun = True 
runMode = 'w'

cityList = [] #keeps track of userinput/cities for history or comparison purposes

print("""
        Welcome to the City-data app. Find out information about a city (ex: Louisville, Kentucky)
        

""")


def chooseCity(menuChoice):
    responses = getWeather(menuChoice)
    return responses  #returns [ response.status_code, cityState, response.json()]

while True:
    if len(cityList)>0:
        graphOption = """  
        2.) Type '2' to see a history of cities that you have obtained information about
            or
        3.) Type '3' to see a graph of populations for the diffrent cities you've looked up so far.
            or
        4.) Type '4' to see a graph of population density for the differnet cities you've looked up so far.
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
        cityData = chooseCity(menuChoice.title()) # using .title() helps avoid some errors
        if cityData[0] != 200:
            print("You entered {} but that wasn't found. Please try again. Please use the format of 'Louisville, Kentucky'".format(cityData[1]))
            print(cityData[0])
        else:
            try:
                b = CityInfo(cityState = cityData[1], weather = cityData[2]) ## creates an instance of CityInfo class passing in the cityRequest
                b.weatherInfo(cityState = cityData[1])
                c = getWiki(cityState = cityData[1])  #Creates a getWiki Object for the target city
                wikiOutput = c.returnWikiInfo(cityState = cityData[1]) #uses scraping of getWiki object just created to return the termLineHeader array as wikiOutput
                names_of_columns = ['City']
                names_of_columns.extend([i[2] for i in wikiOutput ])  #combine the two data list comprehensions/loops??
                data_for_columns = [cityData[1]]
                data_for_columns.extend([i[4] for i in wikiOutput ])
                firstRun, runMode = csv_export.exportToCSV(names_of_columns, data_for_columns, firstRun, runMode) # runs the csv exporter and gives/gets info on mode and firstRun
                cityList.append(cityData[1])
            except ValueError as err:
                print(err, "Error. Well that didn't go as planned...")
            except PermissionError as err:
                print("Permission was denied. Is the Excel file open?", err)             
            except:
                print("Main.py had an error")#add better error message



