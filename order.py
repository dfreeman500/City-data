from city import CityInfo
import csv_export
from cityDatabase import db_entry

red = "\033[0;31m"
end="\033[0m"


#order of operations for both main.py and flask_app.py
def orderOfOps(firstRun,runMode, menuChoice, cityList, requestor):
    cityOutput=[]
    justHeader=[]
    city = CityInfo(menuChoice.title()) #Creates instance of CityInfo class
    responses = city.validate_by_weather_api()  #returns [ response.status_code, cityState, response.json()]

    if responses[0] != 200:
        print(red+ "You entered '{}' but that returned an error {}. You may have misspelled the city, state -  Please try again. Please use the format of 'Louisville, Kentucky'".format(responses[1], responses[0]) + end)
        cityList
        cityOutput=[]
    else:
        try:
            temp = city.print_temp(responses[2])           
            cityOutput, justHeader = city.return_wiki_info(city_state = responses[1], temp=temp) #uses scraping of getWiki object just created to return the termLineHeader array as cityOutput
            names_of_columns = justHeader
            rowData = []
            rowData.extend([i[4] for i in cityOutput ])
            firstRun, runMode = csv_export.export_to_csv(names_of_columns, rowData, firstRun, runMode, filename='city_data.csv') # runs the csv exporter and gives/gets info on mode and firstRun
            if requestor =="main":
                cityList.append(responses[1])
            db_entry(justHeader, rowData)
        except ValueError as err:
            print(red + str(err) + "There was value error in Main.py" + end)

        except PermissionError as err:
            print(red + """
            
            Permission was denied. Unable to save to city_data.csv Is the file open?
            
            """, str(err) + end)             
        except AttributeError as err:
            print(red+ str(err)+ """
            
            The Openweather api may have determined or converted your input as a valid location, but the wikipedia url above
            lacks the HTML structure needed to scrape city information effectively. It was not added to the csv file.

            """+ end)
        except UnboundLocalError as err:
            print(red+ str(err) + """
                variable referenced before assignment
            """ +end)

                
    return firstRun, runMode, cityOutput, cityList, justHeader