from City import CityInfo
# import os
import time
from Weather import getWeather
from wiki import getWiki
import csv_export

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
    # os.system('cls||clear')


    menuChoice = input("""


    
        1.) Enter a city, state (ex: 'Louisville, Kentucky') to find out information about it
            or 
        2.) Type '2' to see a history of cities that you have obtained information about
            or
        3.) Type 'exit' to exit

        """)

    if menuChoice.lower() == "exit" or menuChoice=="3":
        break

    if menuChoice == '2':
        print("Here are the cities you've found data on and info is now in csv file:")
        for x in cityList:
            print(x)
    
    else:
        cityData = chooseCity(menuChoice.title()) # using .title() helps avoid some errors
        # print(cityData[0])
        if cityData[0] != 200:
            print("You entered {} but that wasn't found. Please try again. Please use the format of 'Louisville, Kentucky'".format(cityData[1]))

        else:

            try:
                # print(cityData[2])
                b = CityInfo(cityState = cityData[1], weather = cityData[2]) ## creates an instance of CityInfo class passing in the cityRequest
                b.weatherInfo(cityState = cityData[1])
                c = getWiki(cityState = cityData[1])  #Creates a getWiki Object for the target city
                # wikiOutput = c.returnWikiInfo(cityState = cityData[1])
                # print(c.returnWikiInfo(cityState = cityData[1]))
                wikiOutput = c.returnWikiInfo(cityState = cityData[1]) #uses scraping of getWiki object just created to return the termLineHeader array as wikiOutput
                names_of_columns = ['City']
                names_of_columns.extend([i[2] for i in wikiOutput ])  #combine the two data list comprehensions/loops??
                data_for_columns = [cityData[1]]
                data_for_columns.extend([i[4] for i in wikiOutput ])
                # for i in c.returnWikiInfo(cityState = cityData[1]):
                #     print(i[4])
                # print("")
                # print("names of columns to go into csv file: ", names_of_columns)
                # print("data to go into csv file: ", data_for_columns)
                # names_of_columns = [cityData[1]]
                firstRun, runMode = csv_export.exportToCSV(names_of_columns, data_for_columns, firstRun, runMode) # runs the csv exporter and gives/gets info on mode and firstRun

                cityList.append(cityData[1])


            except:
                print("Error. Well that didn't go as planned...") #add better error message



