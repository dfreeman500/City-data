from city import CityInfo
import csv_export

#order of operations for both main.py and flask_app.py
def orderOfOps(firstRun,runMode, menuChoice, cityList, requestor):
    wikiOutput=[]
    justHeader=[]
    city = CityInfo(menuChoice.title())
    responses = city.validateByWeatherAPI()  #returns [ response.status_code, cityState, response.json()]

    if responses[0] != 200:
        print("You entered {} but that returned an error {}. You may have misspelled the city, state -  Please try again. Please use the format of 'Louisville, Kentucky'".format(responses[1], responses[0]))
        cityList
        wikiOutput=[]
    else:
        try:
            temp = city.printTemp(responses[2])           
            wikiOutput, justHeader = city.returnWikiInfo(cityState = responses[1], temp=temp) #uses scraping of getWiki object just created to return the termLineHeader array as wikiOutput
            names_of_columns = justHeader
            data_for_columns = []
            data_for_columns.extend([i[4] for i in wikiOutput ])
            firstRun, runMode = csv_export.exportToCSV(names_of_columns, data_for_columns, firstRun, runMode) # runs the csv exporter and gives/gets info on mode and firstRun
            if requestor == "main":
                cityList.append(responses[1])
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
                
    return firstRun, runMode, wikiOutput, cityList, justHeader