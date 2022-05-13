import api
import requests
from bs4 import BeautifulSoup
import re
import search_array

class CityInfo:
    def __init__(self, city_state):
        self.city_state = city_state

    #Validates the city by looking it up from openweathermap.org returns status code, city/state, weather info
    def validate_by_weather_api(self):
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(self.city_state, api.OPEN_WEATHER_API))
        return [ response.status_code, self.city_state, response.json()]


    #Prints the weather statement for the console app
    def print_temp(self, weather):
        self.weather = weather
        blue="\033[0;34m"
        end="\033[0m"
        print(blue +"*"*100 +end)
        print("The temperature in {} is {} degrees Fahrenheit but it feels like {}.".format(self.city_state, self.weather["main"]["temp"],self.weather["main"]["feels_like"] ))
        return self.weather["main"]["temp"]

    #Scrapes wikipedia and returns info
    def return_wiki_info(self, city_state, temp):
        self.city_state = city_state
        self.temp = temp

        term_line_header=search_array.term_line_header(self.city_state,self.temp)

        #category and otherMembers - help the program determine if in the population, area, or other section as search terms are not unique between these areas
        category = "other" 
        other_members = ["Mayor","Website","Nickname","Demonym","Motto","MajorAirports","Primary","Secondary", "Airport", "Rapid", "Time"]

        url = ''.join(['https://en.wikipedia.org/wiki/', self.city_state]).replace(' ', '_')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features='lxml')
        table = soup.find('table', attrs={'class':'infobox ib-settlement vcard'})

        print(url)
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
                for member in other_members:
                    if re.sub(r'\W+', '', row.text).startswith(member):
                        category = "other"
                #iterate through termLineHeader, if the current row from bs4 starts with the search term and the category matches - set variable and print the td
                for item in term_line_header:
                    if item[3]=="skip":
                        continue
                    if re.sub(r'\W+', '', row.text).startswith(item[0])  and item[3]==category: 
                            # print(row.text)
                            if row.text != '': #Only print for info that is present
                                cleaned_td = re.sub(r"\[\d+\]", " ", row.td.text) #removes citations numbers
                                cleaned_td_stripped = cleaned_td.replace(u"\u2022","")
                                cleaned_td_stripped = cleaned_td.replace("\xa0"," ") #removes nonbreaking space
                                print(item[1], cleaned_td_stripped)
                                item[4] = cleaned_td_stripped
            except:
                print("error")

        just_header=[] # sends just the header info - makes it easier in flask in case someone sends only blank forms or jibberish info
        for item in term_line_header:
            just_header.append(item[2])

        return term_line_header, just_header