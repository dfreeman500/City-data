import graph_data
import order
from city_database import db_loop

red = "\033[0;31m"
yellow="\033[0;33m"
blue="\033[0;34m"
end="\033[0m"

# firstRun and runMode are for csv exporter so header is only exported the first time
first_run = True 
run_mode = 'w'

city_list = [] #keeps track of cities that have been stored into the csv file

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
    if len(city_list)>0:
        graph_option = """  
        2.) Type '2' to see a history of cities that have been loaded into the csv.
            or
        3.) Type '3' to see a graph of population density for the different cities.
            or
        4.) Type '4' to access the database of cities
        """
    else:
        graph_option = ''

    menu_choice = input(yellow + " "*8 + """="""*100 + end + """
        1.) Enter a city, state (ex: 'Miami, Florida') to find out information about it
            or {}       
            Type 'exit' to exit
        """.format(graph_option)+ yellow + 
    """-->""")

    if menu_choice.lower() == "exit" or menu_choice.lower()=="e":
        break

    elif menu_choice == '2' and len(city_list)>0:
        print(blue + "*" *50 +end)
        print("Number of cities with data in the csv file: {}".format(len(city_list)))
        for city in enumerate(city_list, start = 1):
            print(city)
        continue

    # elif menuChoice =='3' and len(cityList)>0:
    #     graph_data.graphPop()
    #     continue

    elif menu_choice =='3' and len(city_list)>0:
        graph_data.graph_pop_density()
        continue

    elif menu_choice =='4' and len(city_list)>0:
        db_loop()
        continue

    else:
        #checks for obvious duplicate from current run
        collapsed_input = menu_choice.title().replace(' ','')
        collapsed_list = [i.replace(' ','') for i in city_list]
        if collapsed_input in collapsed_list:
            print("{} was already entered - it was not added to the csv".format(menu_choice))
        else:
            first_run, run_mode, menu_choice, city_list, just_header = order.order_of_ops(first_run, run_mode, menu_choice, city_list, requestor="main")
        

        