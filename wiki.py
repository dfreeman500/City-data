import requests
from bs4 import BeautifulSoup
import re


class getWiki:
    def __init__(self, cityState):
        self.cityState = cityState

        
        # print(self.cityState)
        url = ''.join(['https://en.wikipedia.org/wiki/', self.cityState])
        # print("before request")
        r = requests.get(url)
        # print("after request")
        # print(len(r.text))
        # print(r.text)

        soup = BeautifulSoup(r.text, features='lxml')
        print(url)
        # print(soup.title)
        # print(soup.title.string)
        # print(soup.a('infobox geography vcard'))

        data = []
        table = soup.find('table', attrs={'class':'infobox geography vcard'})
        # print(table)
        table_body = table.find('tbody')

        # print(table_body)
        rows = table_body.find_all('tr')
        popAreaTest = False #helps the program determine if in the population or area section

        for row in rows:
            cols = row.find_all('td')
            # print(cols)
            cols = [item.text.strip() for item in cols]
            data.append([item for item in cols if item]) # Get rid of empty values

#Political,Contact, Names, Extraneous
            if re.sub(r'\W+', '', row.text).startswith("Mayor"): # Gets rid of non alpha numeric items
                print("The mayor is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Website"): # Gets rid of non alpha numeric items
                print("The website is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Nickname"): # Gets rid of non alpha numeric items
                print(cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Demonym"): # Gets rid of non alpha numeric items
                print("Demonym: ", cols[0])
            if row.text.startswith("Area code"): # Gets rid of non alpha numeric items
                print("Area Code: ", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Motto"): # Gets rid of non alpha numeric items
                print(cols[0])

#Population
            if re.sub(r'\W+', '', row.text).startswith("Population"): # Gets rid of non alpha numeric items
                popAreaTest = "pop"
            if re.sub(r'\W+', '', row.text).startswith("Total") and popAreaTest == "pop": # Gets rid of non alpha numeric items
                print("The total population is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Estimate") and popAreaTest == "pop": # Gets rid of non alpha numeric items
                print("The total estimated population is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Consolidated") and popAreaTest == "pop": # Gets rid of non alpha numeric items
                print("The consolidated population is", cols[0])
            
            
             
            if re.sub(r'\W+', '', row.text).startswith("Rank") and popAreaTest == "pop": # Gets rid of non alpha numeric items
                print("The city's population rank is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Density") and "rank" not in row.text and popAreaTest == "pop": # Gets rid of non alpha numeric items
                print("The city's population density is", cols[0])
            
            if re.sub(r'\W+', '', row.text).startswith("Demonym"): # tells progam it is no longer dealing with pop or area
                popAreaTest = "dem"



#Time zone
            if re.sub(r'\W+', '', row.text).startswith("Time"): # Gets rid of non alpha numeric items
                print("The Time zone is", cols[0])
            
            
#Geographical
            if re.sub(r'\W+', '', row.text).startswith("Area"): # Gets rid of non alpha numeric items
                popAreaTest = "area"
            if re.sub(r'\W+', '', row.text).startswith("Total") and popAreaTest=="area": # Gets rid of non alpha numeric items
                print("The Total area is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Land") and popAreaTest=="area": # Gets rid of non alpha numeric items
                print("The Land area is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Waterways"): # Gets rid of non alpha numeric items
                print("The waterways are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Elevation"): # Gets rid of non alpha numeric items
                print("The elevation is", cols[0])

            
#Airports/Transportation
            if re.sub(r'\W+', '', row.text).startswith("MajorAirports"): # Gets rid of non alpha numeric items
                print("The major airports are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Primary"): # Gets rid of non alpha numeric items
                print("Primary Airport:", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Secondary"): # Gets rid of non alpha numeric items
                print("Secondary Airports:", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Airport"): # Gets rid of non alpha numeric items
                print("The airports are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Rapid"): # Gets rid of non alpha numeric items
                print("Rapid Transit:", cols[0])               