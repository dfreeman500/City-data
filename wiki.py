import requests
from bs4 import BeautifulSoup
import re


class getWiki:
    def __init__(self, cityState):
        self.cityState = cityState

        
        # print(self.cityState)
        url = ''.join(['https://en.wikipedia.org/wiki/', self.cityState])

        r = requests.get(url)
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
        populationTest = False #Tells the program that we are now in the population section

        for row in rows:
            cols = row.find_all('td')
            # print(cols)
            cols = [item.text.strip() for item in cols]
            data.append([item for item in cols if item]) # Get rid of empty values

            if re.sub(r'\W+', '', row.text).startswith("Mayor"): # Gets rid of non alpha numeric items
                print("The mayor is", cols[0])


            if re.sub(r'\W+', '', row.text).startswith("Population"): # Gets rid of non alpha numeric items
                populationTest = True
            if re.sub(r'\W+', '', row.text).startswith("Total") and populationTest == True: # Gets rid of non alpha numeric items
                print("The total population is", cols[0])
                populationTest = False  #Needs to be last in population group



            if re.sub(r'\W+', '', row.text).startswith("Time"): # Gets rid of non alpha numeric items
                print("The Time zone is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Land"): # Gets rid of non alpha numeric items
                print("The Land area is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Area"): # Gets rid of non alpha numeric items
                print("The area code is", cols)
            # if re.sub(r'\W+', '', row.title).startswith("Consolidated city-county"): # Gets rid of non alpha numeric items
            #     print("The population is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Airport"): # Gets rid of non alpha numeric items
                print("The airports are", cols[0])

            if re.sub(r'\W+', '', row.text).startswith("Waterways"): # Gets rid of non alpha numeric items
                print("The waterways are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Website"): # Gets rid of non alpha numeric items
                print("The website is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Motto"): # Gets rid of non alpha numeric items
                print("The motto is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Elevation"): # Gets rid of non alpha numeric items
                print("The elevation is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Nickname"): # Gets rid of non alpha numeric items
                print(cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Demonym"): # Gets rid of non alpha numeric items
                print("Demonym: ", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Major"): # Gets rid of non alpha numeric items
                print("The major airports are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Primary"): # Gets rid of non alpha numeric items
                print("Primary Airport:", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Secondary"): # Gets rid of non alpha numeric items
                print("Secondary Airports:", cols[0])

            if re.sub(r'\W+', '', row.text).startswith("Rapid"): # Gets rid of non alpha numeric items
                print("Rapid Transit:", cols[0])               