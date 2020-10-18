import csv
from wiki import getWiki

# with open('city_data.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ')
  
#     spamwriter.writerow(['dan'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def exportToCSV(header, rowData, firstRun, runMode):
    with open('city_data.csv', mode=runMode , encoding='utf-8') as csv_file:
        # print("I am running csv")
        # print("here is header", header)
        # print("here is row data", rowData )
        # print(firstRun)

        # writer = csv.DictWriter(csv_file, fieldnames=header, lineterminator='\n')
        linewriter = csv.writer(csv_file, lineterminator='\n')
        if firstRun == True: # prints header info
            linewriter.writerow(header) 
            firstRun = False
            runMode = 'a'
        linewriter.writerow(rowData) 
        # print(firstRun)

    return firstRun, runMode
        
