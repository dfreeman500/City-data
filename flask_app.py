from flask import (Flask, render_template, redirect, 
                    url_for, request, make_response, send_file)
import weather
import csv_export
import city
import wiki
from weather import getWeather
from wiki import GetWiki
import csv_export
import graph_data
import order
from threading import Thread #needed because mtaplotlib is called outside of main loop
import threading
import search_array


app = Flask(__name__)

cityList=[]
cityBatch =[]
wikiBatch = []
firstRun = True 
runMode = 'w'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/city_info',methods=['POST', 'GET']) #only be accessible if you POST to it
def city_info():
    firstRun = True 
    runMode = 'w'
    wikiOutput=[]
    cityList=[]
    wikiBatch=[]

    data = dict(request.form)
    for x in data.values():
        cityList.append(x)
    # print(cityList)

    for city in cityList:
        firstRun, runMode, wikiOutput, cityList, justHeader = order.orderOfOps(firstRun,runMode, menuChoice=city, cityList = cityList, requestor="flask_app")
        wikiBatch.append(wikiOutput) #puts the termLineHeader for each city into a batch

    unpopulatedTLH = search_array.termLineHeader("NoCity", "72")
    justHeader= [item[2] for item in unpopulatedTLH]
    # print("this is justheader", justHeader)
    
    validCitiesList = [] #
    for item in wikiBatch:
        if len(item)>0:
            # print(item)
            validCitiesList.append(item[0][4])
    # print("Valid cities list:", validCitiesList)
    # print(cityList)
    entriesWithNoReturn =[]
    entriesWithNoText=[]
    for item in cityList:       #Find inputs that did not get return values and let the user know
        if len(item)>0 and item.title() not in validCitiesList:
            entriesWithNoReturn.append(item)
        if len(item)<1:
            entriesWithNoText.append(item)
    
    # print("These items did not return a result", entriesWithNoReturn)
    # print("These are items with no text: ", entriesWithNoText, len(entriesWithNoText))
    
    # try:
    #     avoidError1 = threading.Thread(target=graph_data.graphPop)
    #     # avoidError1.setDaemon(True)
    #     avoidError1.start()

    #     avoidError2 = threading.Thread(target=graph_data.graphPopDensity)
    #     # avoidError2.setDaemon(True)
    #     avoidError2.start()
    # except Exception as err:
    #     print("error with threading.Thread, ", err)
    
    # graph_data.graphPopDensity(requestor="flask_app")



    return render_template("city_info.html", cityList=cityList, wikiBatch = wikiBatch, justHeader=justHeader, entriesWithNoReturn=entriesWithNoReturn, entriesWithNoText=entriesWithNoText, validCitiesList=validCitiesList)


@app.route('/download',methods=['POST', 'GET']) #Download CSV file
def downloadCSV ():
    return send_file("city_data.csv", as_attachment=True)

app .run(debug=True, host = '0.0.0.0', port=8000)
