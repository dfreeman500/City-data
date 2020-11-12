from flask import (Flask, render_template, redirect, 
                    url_for, request, make_response, send_file)
import graph_data
import order
from threading import Thread #needed because mtaplotlib is called outside of main loop
import threading
import search_array
import webbrowser

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/city_info',methods=['POST']) 
def city_info():
    firstRun = True 
    runMode = 'w'
    wikiOutput=[] #populated termLineHeader for single city 
    cityList=[] #List of cities/inputs submitted by the user
    wikiBatch=[] #Array of wikiOutputs
    justHeader=[] #Header

    data = dict(request.form) #gets flask data from the request form and puts it in a dict
    for x in data.values():
        cityList.append(x)

    for city in cityList:
        firstRun, runMode, wikiOutput, cityList, justHeader = order.orderOfOps(firstRun,runMode, menuChoice=city, cityList = cityList, requestor="flask_app")
        wikiBatch.append(wikiOutput) #puts the termLineHeader for each city into a batch

    # Gets header information for city_info page
    unpopulatedTLH = search_array.termLineHeader("NoCity", "72")
    justHeader= [item[2] for item in unpopulatedTLH]
    
    #Determines which of the inputs are considered valid, blank, or had no return info so it can inform the user on city_info.html
    validCitiesList = [] 
    for item in wikiBatch:
        if len(item)>0:
            validCitiesList.append(item[0][4])
    entriesWithNoReturn =[]
    entriesWithNoText=[]
    for item in cityList:       
        if len(item)>0 and item.title() not in validCitiesList:
            entriesWithNoReturn.append(item)
        if len(item)<1:
            entriesWithNoText.append(item)
    
    # print("These items did not return a result", entriesWithNoReturn)
    # print("These are items with no text: ", entriesWithNoText, len(entriesWithNoText))
    # argsForGraph= 'requestor="flask_app"'
    # try:
    #     avoidError1 = threading.Thread(target=graph_data.graphPop)
    #     avoidError1.setDaemon(True)
    #     avoidError1.start()
    # except Exception as err:
    #     print("error with threading.Thread, ", err)

    # try:
    #     avoidError2 = threading.Thread(target=graph_data.graphPopDensity)
    #     avoidError2.setDaemon(True)
    #     avoidError2.start()
    # except Exception as err:
    #     print("error with threading.Thread, ", err)
    
    # graph_data.graphPopDensity(requestor="flask_app")

    return render_template("city_info.html", cityList=cityList, wikiBatch = wikiBatch, justHeader=justHeader, entriesWithNoReturn=entriesWithNoReturn, entriesWithNoText=entriesWithNoText, validCitiesList=validCitiesList)

#Download CSV file - cache_timout=0 prevents sending the cached file on repeat download
@app.route('/download',methods=['GET']) 
def downloadCSV ():
    return send_file("city_data.csv", as_attachment=True, cache_timeout="-1") 

if __name__ == "__main__":
    webbrowser.open("http://localhost:5000/")

app.run(debug=True,use_reloader=False)
