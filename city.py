import api
import requests
from bs4 import BeautifulSoup
import re
import search_array

class CityInfo:
    def __init__(self, cityState):
        self.cityState = cityState

    #Validates the city by looking it up from openweathermap.org returns status code, city/state, weather info
    def validateByWeatherAPI(self):
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(self.cityState, api.openWeatherApi))
        return [ response.status_code, self.cityState, response.json()]


    #Prints the weather statement for the console app
    def printTemp(self, weather):
        self.weather = weather
        print("The temperature in {} is {} degrees Fahrenheit but it feels like {}.".format(self.cityState, self.weather["main"]["temp"],self.weather["main"]["feels_like"] ))
        return self.weather["main"]["temp"]

    #Scrapes wikipedia and returns info
    def returnWikiInfo(self, cityState, temp):
        self.cityState = cityState
        self.temp = temp

        termLineHeader=search_array.termLineHeader(self.cityState,self.temp)

        #category and otherMembers - help the program determine if in the population, area, or other section as search terms are not unique between these areas
        category = "other" 
        otherMembers = ["Mayor","Website","Nickname","Demonym","Motto","MajorAirports","Primary","Secondary", "Airport", "Rapid", "Time"]

        url = ''.join(['https://en.wikipedia.org/wiki/', self.cityState]).replace(' ', '_')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features='lxml')
        table = soup.find('table', attrs={'class':'infobox geography vcard'})
        print(url)
        # print(table.prettify())
        for row in table.find_all('tr')[1:]: #finds table rows
            try:
                #This section checks the beginning portion of the row to determine what category to set
                if re.sub(r'\W+', '', row.text).startswith("Population"): 
                    category = "pop"
                if re.sub(r'\W+', '', row.text).startswith("Area"): 
                    category = "area"
                if re.sub(r'\W+', '', row.text).startswith("Densityrank"): 
                     category = "skip"
                if re.sub(r'\W+', '', row.text).startswith("Areacode"): 
                    category = "areacode"
                if ( 
                    re.sub(r'\W+', '', row.text).startswith("MajorAirports") 
                    or re.sub(r'\W+', '', row.text).startswith("Primary") 
                    or re.sub(r'\W+', '', row.text).startswith("Secondary") 
                    or re.sub(r'\W+', '', row.text).startswith("Airport") 
                ): 
                    category = "airport"
                for member in otherMembers:
                    if re.sub(r'\W+', '', row.text).startswith(member):
                        category = "other"
                #iterate through termLineHeader, if the current row from bs4 starts with the search term and the category matches - set variable and print the td
                for item in termLineHeader:
                    if item[3]=="skip":
                        continue
                    if re.sub(r'\W+', '', row.text).startswith(item[0])  and item[3]==category: 
                            # print(row.text)
                            if row.text != '': #Only print for info that is present
                                cleaned_td = re.sub(r"\[\d+\]", " ", row.td.text) #removes citations numbers
                                cleaned_td_stripped = cleaned_td.replace(u"\u2022","")
                                print(item[1], cleaned_td_stripped)
                                item[4] = cleaned_td_stripped
            except:
                print("error")

        justHeader=[] # sends just the header info - makes it easier in flask in case someone sends only blank forms or jibberish info
        for item in termLineHeader:
            justHeader.append(item[2])

        return termLineHeader, justHeader