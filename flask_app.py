from collections import defaultdict
from flask import (Flask, render_template, request, send_file, jsonify)
import graph_data
import order
import search_array
import webbrowser
import json
from markupsafe import Markup
Markup('')


from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.models import ColumnDataSource, ranges, LabelSet, Axis

app = Flask(__name__)

# Index.html route


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/city_info', methods=['POST'])
def city_info():
    first_run = True
    run_mode = 'w'
    city_output = []  # populated termLineHeader for single city
    city_list = []  # List of cities/inputs submitted by the user
    city_batch = []  # Array of cityOutputs
    just_header = []  # Header

    # gets flask data from the user input form and puts it in a dict
    data = dict(request.form)
    for x in data.values():
        city_list.append(x)

    temp_duplicate_check = []
    duplicate_entries = []

    for city in city_list:
        if city in temp_duplicate_check:
            duplicate_entries.append(city)
        else:
            temp_duplicate_check.append(city)
            first_run, run_mode, city_output, city_list, just_header = order.order_of_ops(
                first_run, run_mode, menu_choice=city, city_list=city_list, requestor="flask_app")
            # puts the termLineHeader for each city into a batch
            city_batch.append(city_output)

    # Gets header information for city_info page (particularly important if first city is not valid)
    unpopulated_tlh = search_array.term_line_header("NoCity", "72")
    just_header = [item[2] for item in unpopulated_tlh]

    # Determines which of the inputs are considered valid, blank, or had no return info so it can
    # inform the user on city_info.html. Also, creates and cleans the estimatedpopulationList and
    # populationDensityList for graphs while looping through cityBatch

    valid_cities_list = []
    estimated_population_list = []
    population_density_list = []

    for city in city_batch:
        if len(city) > 0:
            valid_cities_list.append(city[0][4])
            estimated_population_list.append(city[9][4])
            population_density_list.append(city[10][4])

    estimated_population_list = graph_data.clean_pop_input(
        estimated_population_list)
    population_density_list = graph_data.clean_population_density_input(
        population_density_list)

    entries_with_no_return = []
    entries_with_no_text = []
    for item in city_list:
        if len(item) > 0 and item.title() not in valid_cities_list:
            entries_with_no_return.append(item)
        if len(item) < 1:
            entries_with_no_text.append(item)


# Creating the Estimated Population, Population density Bokeh plots if there is at least one validCity
    if len(valid_cities_list) > 0:

        # Wikipedia stopped giving estimated population in their tables

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

        # Creating the Population Density Bokeh plot
        source = ColumnDataSource(
            dict(x=valid_cities_list, y=population_density_list))
        x_label = "City"
        y_label = "Population Density per sq/mi"
        title = "Population Density"
        plot2 = figure(plot_width=175*len(valid_cities_list), plot_height=500, tools="save",
                       x_axis_label=x_label,
                       y_axis_label=y_label,
                       title=title,
                       x_minor_ticks=2,
                       x_range=source.data["x"],
                       y_range=ranges.Range1d(start=0, end=max(population_density_list)+1000))
        plot2.xaxis.major_label_orientation = 45
        labels = LabelSet(x='x', y='y', text='y', level='glyph',
                          x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
        plot2.vbar(source=source, x='x', top='y',
                   bottom=0, width=0.3, color="blue")
        plot2.add_layout(labels)
        script2, div2 = components(plot2)

    else:
        # script1=""
        # div1=""
        script2 = ""
        div2 = ""

    # provide minified BokehJS from library static directory
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    return render_template("city_info.html", city_list=city_list, city_batch=city_batch, just_header=just_header,
                           entries_with_no_return=entries_with_no_return, entries_with_no_text=entries_with_no_text, valid_cities_list=valid_cities_list,
                           # plot_script1=script1, plot_div1=div1,
                           plot_script2=script2, plot_div2=div2, js_resources=js_resources,
                           css_resources=css_resources, duplicate_entries=duplicate_entries, cache_timeout=0)

# Download CSV file - cache_timout=0 prevents sending the cached file on repeat download


@app.route('/download', methods=['GET'])
def download_csv():
    return send_file("city_data.csv", as_attachment=True, cache_timeout=-1)


### LYFT CHALLENGE ####

# write a small web application in one of the above languages (Python/Ruby/Javascript).
# The application only needs to do the following:
# Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
# Return a JSON object with the key “return_string” and a string containing every third letter from the original string
# (e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.
# Note: To see expected behavior you can test against a current working example with the command:
# curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
# For this app post: curl -X POST localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'

@app.route('/test', methods=['POST'])
def lyft_challenge():
    data = request.get_json()
    return {"return_string": data["string_to_cut"][2::3]}

## NO TIME LIMIT ON THIS SIMPLE CACHE!!!!
api_cache = defaultdict(lambda: "Not Present")


@app.route('/api/<city>', methods=['GET'])
def api_route(city):
    if api_cache[city] == "Not Present":
        first_run, run_mode, menu_choice, city_list, just_header = order.order_of_ops(
            first_run=True, run_mode='w', menu_choice=city, city_list=city, requestor="main")

        returned_data = jsonify([{x[2]:x[4]} for x in menu_choice])
        # print(city)
        # print(menu_choice)
        # print(api_cache[city])
        # print(api_cache)

        if len(menu_choice) == 0:
            return "Please enter a valid entry of the form: city, state (ex: Louisville, Kentucky)", 400
        else:
            api_cache[city]=returned_data
            return returned_data, 200
    else:
        print("api is cached")
        return api_cache[city], 203


if __name__ == "__main__":
    webbrowser.open("http://localhost:5000/")

app.run(debug=True, use_reloader=False)
