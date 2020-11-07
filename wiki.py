import requests
from bs4 import BeautifulSoup
import re




class GetWiki:
    def __init__(self, cityState, temp):
        self.cityState = cityState
        self.temp = temp


    def returnWikiInfo(self, cityState, temp):
        self.cityState = cityState
        self.temp = temp

        # Instantiates variables that will be used in termLineHeader
        City = self.cityState
        Temp = self.temp

        Mayor, Website, Nickname, Demonym, Areacode = ["","","","",""] 
        Motto, Total_Population, Estimated_Population, Consolidated_Population =["","","",""] 
        Population_Rank, Population_Density, Population_Density_Rank, Total_Land_Area = ["","","",""]    
        Waterways, Elevation, Major_Airports, Primary_Aiport, Secondary_Airports =["","","","",""] 
        Airports, Rapid_Transit, Time_Zone  = ["","",""] 

        #Each list in array has: search (1)TERM, (2)LINE to print, (3)HEADER for csv file, (4)CATEGORY - for scraping, (5)VARIABLE to store scraped info
        termLineHeader = [ 
            ["City", "", "City", "skip", City],
            ["Temp", "Temp is", "Temp", "skip", Temp ],
            ["Mayor", "The Mayor is", "Mayor", "other", Mayor],
            ["Website", "The website is", "Website", "other", Website],
            ["Nickname", '', "Nickname", "other", Nickname],
            ["Demonym", "Demonym: ", "Demonym", "other", Demonym],
            ["Areacode", "Area Code: ", "Area_Code", "areacode", Areacode],
            ["Motto", '', "Motto", "other", Motto],

            ["Total", "The total population is", "Total_Population", "pop", Total_Population],
            ["Estimate", "The total estimated population is", "Estimated_Population", "pop", Estimated_Population],
            ["Consolidated", "The consolidated population is", "Consolidated_Population", "pop", Consolidated_Population],
            # ["Rank", "The city's population rank is ", "Population_Rank", "pop", Population_Rank],
            ["Density", "The city's population density is", "Population_Density", "pop", Population_Density],

            # ["Densityrank", "The city's population density rank is", "Population_Density_Rank", "poprank", Population_Density_Rank],

            # ["Area", "The total area is", "Total_Area", "area", Total_Area],
            ["Land", "The total land area is ", "Total_Land_Area", "area", Total_Land_Area],
            # ["Waterways", "The waterways are ", "Waterways", "area", Waterways],
            ["Elevation", "The elevation is ", "Elevation", "area", Elevation],

            # ["MajorAirports", "The major airports are", "Airports", "airport", Major_Airports],
            # ["Primary", "Primary Aiport: ", "Airports", "airport", Primary_Aiport],
            # ["Secondary", "Secondary Airports: ", "Airports", "airport", Secondary_Airports],
            # ["Airport", "The airports are", "Airports", "airport", Airports],
            ["Rapid", "Rapid Transit:", "Rapid_Transit", "other", Rapid_Transit],
            ["Time", "The Time zone is ", "Time_Zone", "other", Time_Zone],
        ] 

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
