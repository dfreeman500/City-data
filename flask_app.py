from flask import (Flask, render_template, request, send_file)
import graph_data
import order
import search_array
import webbrowser

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.models import ColumnDataSource, ranges, LabelSet, Axis

app = Flask(__name__)

#Index.html route
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/city_info',methods=['POST']) 
def city_info():
    firstRun = True 
    runMode = 'w'
    cityOutput=[] #populated termLineHeader for single city 
    cityList=[] #List of cities/inputs submitted by the user
    cityBatch=[] #Array of cityOutputs
    justHeader=[] #Header

    data = dict(request.form) #gets flask data from the user input form and puts it in a dict
    for x in data.values():
        cityList.append(x)

    tempDuplicateCheck=[]
    duplicateEntries=[]

    for city in cityList:
        if city in tempDuplicateCheck:
            duplicateEntries.append(city)
        else:
            tempDuplicateCheck.append(city)
            firstRun, runMode, cityOutput, cityList, justHeader = order.orderOfOps(firstRun,runMode, menuChoice=city, cityList = cityList, requestor="flask_app")
            cityBatch.append(cityOutput) #puts the termLineHeader for each city into a batch

    # Gets header information for city_info page (particularly important if first city is not valid)
    unpopulatedTLH = search_array.termLineHeader("NoCity", "72")
    justHeader= [item[2] for item in unpopulatedTLH]
    
    # Determines which of the inputs are considered valid, blank, or had no return info so it can 
    # inform the user on city_info.html. Also, creates and cleans the estimatedpopulationList and 
    # populationDensityList for graphs while looping through cityBatch

    validCitiesList = [] 
    estimatedPopulationList = []
    populationDensityList = []

    for city in cityBatch:
        if len(city)>0:
            validCitiesList.append(city[0][4])
            estimatedPopulationList.append(city[9][4])
            populationDensityList.append(city[10][4])

    estimatedPopulationList = graph_data.cleanPopInput(estimatedPopulationList)
    populationDensityList = graph_data.cleanPopDensityInput(populationDensityList)

    entriesWithNoReturn =[]
    entriesWithNoText=[]
    for item in cityList:       
        if len(item)>0 and item.title() not in validCitiesList:
            entriesWithNoReturn.append(item)
        if len(item)<1:
            entriesWithNoText.append(item)
    

#Creating the Estimated Population, Population density Bokeh plots if there is at least one validCity
    if len(validCitiesList)>0:

        ## Wikipedia stopped giving estimated population in their tables
    

    #     source = ColumnDataSource(dict(x=validCitiesList,y=estimatedPopulationList))
    #     x_label = "City"
    #     y_label = "Estimated Population"
    #     title = "Estimated Population (not all cities have this info)"
    #     plot1 = figure(plot_width=175*len(validCitiesList), plot_height=500, tools="save",
    #             x_axis_label = x_label,
    #             y_axis_label = y_label,
    #             title=title,
    #             x_minor_ticks=2,
    #             x_range = source.data["x"],
    #             y_range= ranges.Range1d(start=0,end=max(estimatedPopulationList)+5000))
    #     plot1.xaxis.major_label_orientation = 45
    #     labels = LabelSet(x='x', y='y', text='y', level='glyph', 
    #             x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
    #     plot1.vbar(source=source,x='x',top='y',bottom=0,width=0.3,color="green")
    #     plot1.add_layout(labels)
    #     yaxis = plot1.select(dict(type=Axis, layout="left"))[0]
    #     yaxis.formatter.use_scientific = False
    #     script1, div1 = components(plot1)     # Return HTML components to embed a Bokeh plot. The data for the plot is stored directly in the returned HTML.


    #Creating the Population Density Bokeh plot
        source = ColumnDataSource(dict(x=validCitiesList,y=populationDensityList))
        x_label = "City"
        y_label = "Population Density per sq/mi"
        title = "Population Density"
        plot2 = figure(plot_width=175*len(validCitiesList), plot_height=500, tools="save",
                x_axis_label = x_label,
                y_axis_label = y_label,
                title=title,
                x_minor_ticks=2,
                x_range = source.data["x"],
                y_range= ranges.Range1d(start=0,end=max(populationDensityList)+1000))
        plot2.xaxis.major_label_orientation = 45
        labels = LabelSet(x='x', y='y', text='y', level='glyph',            
            x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
        plot2.vbar(source=source,x='x',top='y',bottom=0,width=0.3,color="blue")
        plot2.add_layout(labels)
        script2, div2 = components(plot2)

    else:
        # script1=""
        # div1=""
        script2=""
        div2=""

    #provide minified BokehJS from library static directory
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    return render_template("city_info.html", cityList=cityList, cityBatch = cityBatch, justHeader=justHeader, 
        entriesWithNoReturn=entriesWithNoReturn, entriesWithNoText=entriesWithNoText, validCitiesList=validCitiesList, 
        # plot_script1=script1, plot_div1=div1, 
        plot_script2=script2, plot_div2=div2, js_resources=js_resources, 
        css_resources=css_resources, duplicateEntries=duplicateEntries, cache_timeout=0)

#Download CSV file - cache_timout=0 prevents sending the cached file on repeat download
@app.route('/download',methods=['GET']) 
def downloadCSV ():
    return send_file("city_data.csv", as_attachment=True, cache_timeout=-1) 


if __name__ == "__main__":
    webbrowser.open("http://localhost:5000/")

app.run(debug=True,use_reloader=False)
