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
        firstRun, runMode, wikiOutput, cityList = order.orderOfOps(firstRun,runMode, menuChoice=city, cityList = cityList, requestor="flask_app")
        wikiBatch.append(wikiOutput)

    return render_template("city_info.html", cityList=cityList, wikiBatch = wikiBatch)


@app.route('/download',methods=['POST', 'GET']) #Download CSV file
def downloadCSV ():
    return send_file("city_data.csv", as_attachment=True)

app .run(debug=True, host = '0.0.0.0', port=8000)
