import csv
import os

#header - header for csv from item[2] from termLineHeader array
#rowData - row data taken from item[4] from termLineHeader array
#runMode - sets 'w' vs 'a' depending on the first run of export

#csv exports done per session ('city_data.csv') but also for exporting the persisting db ('city_data_db.csv')

def export_to_csv(header, rowData, first_run, run_mode, filename):
    with open(os.path.join(os.sys.path[0], filename), mode=run_mode , encoding="utf-8-sig") as csv_file: #Tries to create csv in the same directory as .py files
        linewriter = csv.writer(csv_file, lineterminator='\n')
        if first_run == True: # prints header info if it is running for the first time
            linewriter.writerow(header) 
            first_run = False
            run_mode = 'a'
        linewriter.writerow(rowData) 

    return first_run, run_mode
        
