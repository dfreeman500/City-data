from city import CityInfo
import time
from weather import getWeather
from wiki import GetWiki
import csv_export
import graph_data


def chooseCity(menuChoice):
    responses = getWeather(menuChoice)
    return responses  #returns [ response.status_code, cityState, response.json()]

def orderOfOps(firstRun,runMode, menuChoice, cityList, requestor):
    wikiOutput=[]
    cityData = chooseCity(menuChoice.title()) # using .title() helps avoid some errors

    if cityData[0] != 200:
        print("You entered {} but that wasn't found. You may have misspelled the city, state -  Please try again. Please use the format of 'Louisville, Kentucky'".format(cityData[1]))
        print(cityData[0])
        cityList
        wikiOutput=[]
    else:
        try:
            b = CityInfo(cityState = cityData[1], weather = cityData[2]) ## creates an instance of CityInfo class passing in the cityRequest
            temp = b.weatherInfo(cityState = cityData[1])
            c = GetWiki(cityState = cityData[1],temp=temp)  #Creates a getWiki Object for the target city
            
            wikiOutput = c.returnWikiInfo(cityState = cityData[1], temp=temp) #uses scraping of getWiki object just created to return the termLineHeader array as wikiOutput
            names_of_columns = []
            names_of_columns.extend([i[2] for i in wikiOutput ])  #combine the two data list comprehensions/loops??
            data_for_columns = []
            data_for_columns.extend([i[4] for i in wikiOutput ])
            firstRun, runMode = csv_export.exportToCSV(names_of_columns, data_for_columns, firstRun, runMode) # runs the csv exporter and gives/gets info on mode and firstRun
            if requestor == "main":
                cityList.append(cityData[1])
        except ValueError as err:
            print(err, "There was value error in Main.py")

        except PermissionError as err:
            print("""
            
            Permission was denied. Is the Excel file open?
            
            """, err)             
        except AttributeError as err:
            print(err, """
            
            The Openweather api may have determined or converted your input as a valid city, but the url above
            lacks the HTML structure needed to scrape information effectively. It was not added to the csv file.

            """)
        except UnboundLocalError as err:
            print(err, """
                That city wasn't found
            """)
                
    return firstRun, runMode, wikiOutput, cityList