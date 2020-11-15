import matplotlib.pyplot as plt
import pandas
import os


# DRY - have pop and popDensity send here to graph
def graphIt():
    pass

#allows cleaning of data to be used by main (matplotlib) and flask_app (Bokeh)
def cleanPopInput(population):
    new_population = [str(i).replace(',', '').replace('nan','0') for i in population] #replace commas with '' and nan with 0
    for x in range(0,len(new_population)):
        if population[x] == '':
            new_population[x]=0
    new_population = [int(i) for i in new_population] # turns strings into int

    return new_population

#Graphs the population
def graphPop():
    data = pandas.read_csv(os.path.join(os.sys.path[0], 'city_data.csv'))
    cities = data.City.tolist()
    population = data.Estimated_Population.tolist()
    new_population = cleanPopInput(population)
    x_pos = [i for i, _ in enumerate(cities)]
    plt.bar(x_pos, new_population, color='green')
    plt.xlabel("Cities")
    plt.ylabel("Population")
    plt.title("Populations of Various Cities")
    plt.xticks(x_pos, cities)
    plt.xticks(rotation=10)
    plt.show()

#allows cleaning of data to be used by main (matplotlib) and flask_app (Bokeh)
def cleanPopDensityInput(population_density):
    new_population_density = [str(i).replace(',', '').replace('nan','0').split('/') for i in population_density] #replace commas with '' and nan with 0
    population_density_numbers =[]
    for i in new_population_density:
        population_density_numbers.append(i[0])
    population_density_numbers = [float(i) for i in population_density_numbers] # turns strings into floats
    return population_density_numbers

#Graphs population density
def graphPopDensity():
    data = pandas.read_csv(os.path.join(os.sys.path[0], 'city_data.csv'))
    cities = data.City.tolist()
    population_density = data.Population_Density.tolist()
    population_density_numbers = cleanPopDensityInput(population_density)
    x_pos = [i for i, _ in enumerate(cities)]
    plt.bar(x_pos, population_density_numbers, color='green')
    plt.xlabel("Cities")
    plt.ylabel("Population Density per sq mi")
    plt.title("Population Densities of Various Cities")
    plt.xticks(x_pos, cities)
    plt.xticks(rotation=10)

    plt.show()


