# City-data

This console app allows the user to get data on a city using a variety of APIs and webscraping. It works best on American cities but can find information on many non-American cities.

1. **Clone the repo**
2. **Create an api.py file in the main directory and copy and paste the openWeatherApi variable (ex: ' openWeatherApi = "abc123" ') that is given to you into the file and save.**
3. **PIP install the following or use the requirements.txt file:**
    * requests == 2.24.0
    * bs4 == 0.0.1
    * Possibly: lxml == 4.5.2
4. **Run Main.py**




* **Future additions:** 
    * better error handling for wikipedia
    * better scraping
    * better use of files and classes to logically stream line app
    * save city data to variable and export to csv
    * Possibly graph certain numerical values across cities (ex: population, density, land area)
    * GUI

    * ability to take zip codes
    * convert state abbreviations to full state names
    * Capitalize first letter automatically -Done - reduces errors for wikipedia scraping