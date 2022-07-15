import sqlite3
import csv_export


red = "\033[0;31m"
blue="\033[0;34m"
lightblue="\033[0;36m"
white="\033[0;37m"
green="\033[0;32m"
yellow="\033[0;33m"

end="\033[0m"




def db_entry(headerinfo, rowData):

    #Builds table columns based on headerinfo
    table_create = ""
    for x in range(len(headerinfo)):
        table_create += headerinfo[x] +" text"
        if x< len(headerinfo)-1:
            table_create+=", "

    #connect to database
    conn = sqlite3.connect("CITY.db")
    #creates cursor
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cityInfo ({})""".format(table_create))
    cursor.execute("INSERT INTO cityInfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",( rowData[0],rowData[1],rowData[2],
            rowData[3], rowData[4],rowData[5], rowData[6], rowData[7], rowData[8], rowData[9], rowData[10], 
            rowData[11], rowData[12], rowData[13],rowData[14]))
    #commit our command
    conn.commit()
    #close connection - best practice
    conn.close()


def db_display():
    print(yellow +"*"*100 +end)    
    print(red +"*"*100 +end)    


    conn = sqlite3.connect("CITY.db")
    #creates cursor
    cursor = conn.cursor()
    #prints header info then each rowid
    cursor = conn.execute("SELECT rowid, * FROM cityInfo")
    names = [description[0] for description in cursor.description]
    # print(blue +"*"*100 +end)    
    # print(blue, names, end)
    cursor.execute("SELECT rowid, * FROM cityInfo")
    records = cursor.fetchall()
    # for record in records:
    #     print(lightblue, record, end)
    #     print()
    
    if len(records)>0:
        for record in records:
            print(green +"*"*100 +end)    
            for item in range(len(record)):
                print(blue, names[item],": ", end, lightblue, record[item],end)
    else:
        print(green, "There are currently no records in the database.", end)
    return names, records


def db_edit():
    db_display()
    try:
        record_item = int(input("     Which record(rowid) would you like to update? "))
        conn = sqlite3.connect("CITY.db")
        cursor = conn.cursor()
        set_item = input("     Which item in the record would you like to set? ex: 'City', 'Area_Code' --> ")
        update_item = input("     What would you like to set the new item to be? ")

        conn = sqlite3.connect("CITY.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE cityInfo SET {} = '{}' WHERE rowid = {}".format(set_item, update_item, record_item))
        conn.commit()
        conn.close()
        db_display()
    except ValueError as err:
        print(red, "     Please only enter an integer that corresponds to the record: ", err, end)
    except sqlite3.OperationalError as err:
        print(red, "     Please enter the column name exactly (ex: 'Total_Population'). Item {} not edited. ".format(record_item), end)



def db_delete():
    db_display()
    try:
        user_input = int(input("     Which record (rowid) would you like to delete? "))
        conn = sqlite3.connect("CITY.db")
        cursor = conn.cursor()
        cursor.execute("DELETE from cityInfo WHERE rowid = {}".format(user_input))
        conn.commit()
        conn.close()
        db_display()
    except ValueError as err:
        print(red, "     Please only enter an integer that corresponds to the record: ", err, end)

def csv():
    names, records = db_display()
    first_run=True
    run_mode='w'
    user_input = input("     Type 'y' to create a new csv file with all records currently in the db (any other character escapes):")
    if user_input.lower()=='y':
        for record in records:
            try:
                first_run, run_mode = csv_export.export_to_csv(names, record, first_run, run_mode, filename='city_data_db.csv') # runs the csv exporter and gives/gets info on mode and first_run
            except PermissionError as err:
                print(red + """
                
                Permission was denied. Unable to save to city_data.csv Is the file open?
                
                """, str(err) + end)    
        print("     {} entries are now loaded in the csv file.".format(len(records)))
    else:
        pass    


def db_loop():
    while True:
        user_input = input(white+"         What would you like to do with the database: 'q' for quit, 's' to show, 'd' for delete a record, 'e' to edit a record, 'csv' to export the db to csv. ")
        if user_input.lower()=='q':
            break
        elif user_input.lower()=='s':
            db_display()
        elif user_input.lower()=='d':
            db_delete()
        elif user_input.lower()=='e':
            db_edit()
        elif user_input.lower()=='csv':
            csv()