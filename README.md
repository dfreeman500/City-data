# City-data

This console app allows the user to get data on a city using a variety of APIs and webscraping. It works best on American cities but can find informatio non many non-American cities.


* Please create an api.py file in the main directory and copy and paste the openWeatherApi variable into the file and save.

* Please PIP install the following:

    * requests == 2.24.0
    * bs4 == 0.0.1
    * Possibly: lxml == 4.5.2

* Run Main.py


* Future additions: 
    * better error handling for wikipedia
    * better scraping
    * better use of files and classes to logically stream line app
    * save city data to variable and export to csv
    * Possibly graph certain numerical values across cities (ex: population, density, land area)
    * GUI

    * ability to take zip codes
    * convert state abbreviations to full state names
    * Capitalize first letter automatically -Done - reduces errors for wikipedia scraping