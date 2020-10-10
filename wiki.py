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
        # print(soup.title)
        # print(soup.title.string)
        # print(soup.a('infobox geography vcard'))

        data = []
        table = soup.find('table', attrs={'class':'infobox geography vcard'})
        # print(table)
        table_body = table.find('tbody')

        # print(table_body)
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            # print(cols)
            cols = [item.text.strip() for item in cols]
            data.append([item for item in cols if item]) # Get rid of empty values

            if re.sub(r'\W+', '', row.text).startswith("Mayor"): # Gets rid of non alpha numeric items
                print("The mayor is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Total"): # Gets rid of non alpha numeric items
                print("The total population is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Time zone"): # Gets rid of non alpha numeric items
                print("The Time zone is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Land"): # Gets rid of non alpha numeric items
                print("The Land area is", cols[0])
            # if re.sub(r'\W+', '', row.text).startswith("Area code"): # Gets rid of non alpha numeric items
            #     print("The area code is", cols)
            # if re.sub(r'\W+', '', row.title).startswith("Consolidated city-county"): # Gets rid of non alpha numeric items
            #     print("The population is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Airports"): # Gets rid of non alpha numeric items
                print("The airports are", cols[0])

            if re.sub(r'\W+', '', row.text).startswith("Waterways"): # Gets rid of non alpha numeric items
                print("The waterways are", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Website"): # Gets rid of non alpha numeric items
                print("The website is", cols[0])
            if re.sub(r'\W+', '', row.text).startswith("Motto"): # Gets rid of non alpha numeric items
                print("The motto is", cols[0])