import csv
import os

#header - header for csv from item[2] from termLineHeader array
#rowData - row data taken from item[4] from termLineHeader array
#runMode - sets 'w' vs 'a' depending on the first run of export

#csv exports done per session ('city_data.csv') but also for exporting the persisting db ('city_data_db.csv')

def exportToCSV(header, rowData, firstRun, runMode, filename):
    with open(os.path.join(os.sys.path[0], filename), mode=runMode , encoding="utf-8-sig") as csv_file: #Tries to create csv in the same directory as .py files
        linewriter = csv.writer(csv_file, lineterminator='\n')
        if firstRun == True: # prints header info if it is running for the first time
            linewriter.writerow(header) 
            firstRun = False
            runMode = 'a'
        linewriter.writerow(rowData) 

    return firstRun, runMode
        
