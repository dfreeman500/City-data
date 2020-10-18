import requests
from bs4 import BeautifulSoup
import re


class getWiki:
    def __init__(self, cityState):
        self.cityState = cityState

    def returnWikiInfo(self, cityState):
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
        popAreaTest = "other" #helps the program determine if in the population, area, or other section as search terms are not unique between these areas


        # Instantiates variables that will be used in termLineHeader
        Mayor, Website, Nickname, Demonym, Areacode = ["","","","",""] 
        Motto, Total_Population, Estimated_Population, Consolidated_Population =["","","",""] 
        Population_Rank, Population_Density, Population_Density_Rank, Total_Land_Area = ["","","",""]    
        Waterways, Elevation, Major_Airports, Primary_Aiport, Secondary_Airports =["","","","",""] 
        Airports, Rapid_Transit, Time_Zone  = ["","",""] 

        #Each list in array has: search term, line to print, header for csv file, category (for scraping), returned info to store in variable
        termLineHeader = [ 
            ["Mayor", "The Mayor is", "Mayor", "other", Mayor],
            ["Website", "The website is", "Website", "other", Website],
            ["Nickname", '', "Nickname", "other", Nickname],
            ["Demonym", "Demonym: ", "Demonym", "other", Demonym],
            ["Areacode", "Area Code: ", "Area_Code", "areacode", Areacode],
            ["Motto", '', "Motto", "other", Motto],

            ["Total", "The total population is", "Total_Population", "pop", Total_Population],
            ["Estimate", "The total estimated population is", "Estimated_Population", "pop", Estimated_Population],
            ["Consolidated", "The consolidated population is", "Consolidated_Population", "pop", Consolidated_Population],
            ["Rank", "The city's population rank is ", "Population_Rank", "pop", Population_Rank],
            ["Density", "The city's population density is", "Population_Density", "pop", Population_Density],

            ["Densityrank", "The city's population density rank is", "Population_Density_Rank", "poprank", Population_Density_Rank],

            # ["Area", "The total area is", "Total_Area", "area", Total_Area],
            ["Land", "The total land area is ", "Total_Land_Area", "area", Total_Land_Area],
            ["Waterways", "The waterways are ", "Waterways", "area", Waterways],
            ["Elevation", "The elevation is ", "Elevation", "area", Elevation],

            ["MajorAirports", "The major airports are", "Major_Airports", "other", Major_Airports],
            ["Primary", "Primary Aiport: ", "Primary_Aiport", "other", Primary_Aiport],
            ["Secondary", "Secondary Airports: ", "Secondary_Airports", "other", Secondary_Airports],
            ["Airport", "The airports are", "Airports", "other", Airports],
            ["Rapid", "Rapid Transit:", "Rapid_Transit", "other", Rapid_Transit],
            ["Time", "The Time zone is ", "Time_Zone", "other", Time_Zone],
        ] 


        for row in rows:
            cols = row.find_all('td')
            # print(cols)
            cols = [item.text.strip() for item in cols]
            data.append([item for item in cols if item]) # Get rid of empty values

            # Change category for scraping
            if re.sub(r'\W+', '', row.text).startswith("Population"): 
                popAreaTest = "pop"
            if re.sub(r'\W+', '', row.text).startswith("Area"): 
                popAreaTest = "area"
            if re.sub(r'\W+', '', row.text).startswith("Densityrank"): 
                popAreaTest = "poprank"
            if re.sub(r'\W+', '', row.text).startswith("Areacode"): 
                popAreaTest = "areacode"
            if re.sub(r'\W+', '', row.text).startswith("Demonym") or re.sub(r'\W+', '', row.text).startswith("Time") or re.sub(r'\W+', '', row.text).startswith("Elevation") :
                popAreaTest = "other"

            # print(row.text)
            # print(popAreaTest)
            for item in termLineHeader:
                if re.sub(r'\W+', '', row.text).startswith(item[0])  and item[3]==popAreaTest: 
                    try:
                        if cols[0] != '': #Only print for info that is present
                            print(item[1], cols[0])
                        item[4] = cols[0]
                    except:
                        print("error") # add better error message

        # print(termLineHeader)
        return termLineHeader
