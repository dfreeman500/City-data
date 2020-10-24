# City-data

This console app allows the user to get data on a city using the Openweather API and webscraping. You enter a city and state and the openweather api searches for the temperature. Then the program generates a url and returns the page. The program scrapes the information from the page and stores the info into a csv file. You can read the csv and show bar graphs of estimated population and population density (not all cities provide this information).  The program works best on American cities.
#

# Code Louisville Features Met:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program 
    ##### * Main.py has a master loop 


* Create a class, then create at least one object of that class and populate it with data
    ##### * City.py and wiki.py utilize a class


* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    ##### * Main.py uses cityList variable to store list of cities, wiki.py uses termLineHeader array to temporarily store scraped data


* Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
    ##### * graph_data.py reads city_data.csv to display bar graphs


* Create and call at least 3 functions, at least one of which must return a value that is used
    ##### * multiple functions, wiki.py has returnWikiInfo which returns termLineHeader array


* Connect to an external/3rd party API and read data into your app
    ##### * Weather.py connects to openweathermap.org API

* Visualize data in a graph, chart, or other visual representation of data
    ##### * graph_data.py uses matplotlib and pandas to graph data from a csv


* Implement a “scraper” that can be fed a type of file or URL and pull information off of it.
    ##### * Bs4 is used to scrape wikipedia information




#
# Instructions:

1. **Clone the repo**
2. **Create an api.py file in the main directory and copy and paste the openWeatherApi variable (ex: ' openWeatherApi = "abc123" ') that is given to you into the file and save.**
3. **PIP install the following or use the requirements.txt file:**
    * requests == 2.24.0
    * bs4 == 0.0.1
    * lxml == 4.5.2
    * matplotlib == 3.3.2
    * pandas == 1.1.0
4. **Run Main.py**

#

* **Future additions:** 
    * better use of files and classes to logically stream line app
    * GUI
    * ability to take zip codes
    * convert state abbreviations to full state names
