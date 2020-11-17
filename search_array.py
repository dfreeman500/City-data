
#Each item in termLineHeader has: search (1)TERM, (2)LINE to print, (3)HEADER for csv file/flask app, (4)CATEGORY - for scraping, 
# (5)VARIABLE to store scraped info. Placing in separate file allows easier access for flask_app


def termLineHeader(city, temp):
    City=city
    Temp=temp

    Mayor, Website, Nickname, Demonym, Areacode = ["","","","",""] 
    Motto, Total_Population, Estimated_Population, Consolidated_Population =["","","",""] 
    Population_Rank, Population_Density, Population_Density_Rank, Total_Land_Area = ["","","",""]    
    Waterways, Elevation, Major_Airports, Primary_Aiport, Secondary_Airports =["","","","",""] 
    Airports, Rapid_Transit, Time_Zone  = ["","",""] 

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
        # ["Consolidated", "The consolidated population is", "Consolidated_Population", "pop", Consolidated_Population],
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

    return termLineHeader