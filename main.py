import graph_data
import order
from cityDatabase import dbLoop

red = "\033[0;31m"
yellow="\033[0;33m"
blue="\033[0;34m"
end="\033[0m"

# firstRun and runMode are for csv exporter so header is only exported the first time
firstRun = True 
runMode = 'w'

cityList = [] #keeps track of cities that have been stored into the csv file

print(red + """
        Welcome to the City-data app, where you can find out all kinds of information about a city! 
        This app allows the user to get data on a city using the Openweather API and webscraping 
        from wikipedia. You enter a city and state and the openweather api searches for the temperature. 
        If the input is 'valid' and a temperature is returned, the program generates a wikipedia url. If the 
        url is valid and has enough structure for scraping, the program scrapes the information from the page 
        and stores the info into a csv file (city_data.csv). Each city provides different information so specific
        fields may not always be available.
""" + end )

while True:
    if len(cityList)>0:
        graphOption = """  
        2.) Type '2' to see a history of cities that have been loaded into the csv.
            or
        3.) Type '3' to see a graph of estimated populations"""+ yellow +" (some cities on wikipedia do not show estimated population)."""+end+"""
            or
        4.) Type '4' to see a graph of population density for the different cities.
            or
        5.) Type '5' to access the database of cities
        """
    else:
        graphOption = ''

    menuChoice = input(yellow + " "*8 + """="""*100 + end + """
        1.) Enter a city, state (ex: 'Miami, Florida') to find out information about it
            or {}       
            Type 'exit' to exit
        """.format(graphOption)+ yellow + 
    """-->""")

    if menuChoice.lower() == "exit" or menuChoice.lower()=="e":
        break

    elif menuChoice == '2' and len(cityList)>0:
        print(blue + "*" *50 +end)
        print("Number of cities with data in the csv file: {}".format(len(cityList)))
        for city in enumerate(cityList, start = 1):
            print(city)
        continue

    elif menuChoice =='3' and len(cityList)>0:
        graph_data.graphPop()
        continue

    elif menuChoice =='4' and len(cityList)>0:
        graph_data.graphPopDensity()
        continue

    elif menuChoice =='5' and len(cityList)>0:
        dbLoop()
        continue

    else:
        #checks for obvious duplicate from current run
        collapsedInput = menuChoice.title().replace(' ','')
        collapsedList = [i.replace(' ','') for i in cityList]
        if collapsedInput in collapsedList:
            print("{} was already entered - it was not added to the csv".format(menuChoice))
        else:
            firstRun, runMode, menuChoice, cityList, justHeader = order.orderOfOps(firstRun, runMode, menuChoice, cityList, requestor="main")
        

        