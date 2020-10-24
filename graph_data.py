import matplotlib.pyplot as plt
import pandas



# def graphIt():
#     pass




#Graphs the population
def graphPop():
    data = pandas.read_csv('city_data.csv')

    cities = data.City.tolist()
    population = data.Estimated_Population.tolist()
    new_population = [str(i).replace(',', '').replace('nan','0') for i in population] #replace commas with '' and nan with 0
    new_population = [int(i) for i in new_population] # turns strings into int

    x_pos = [i for i, _ in enumerate(cities)]

    plt.bar(x_pos, new_population, color='green')
    plt.xlabel("Cities")
    plt.ylabel("Population")
    plt.title("Populations of Various Cities")

    plt.xticks(x_pos, cities)

    plt.show()


#Graphs population density
def graphPopDensity():
    # colnames = ['City', 'Estimated_Population']
    data = pandas.read_csv('city_data.csv')

    cities = data.City.tolist()
    population_density_numbers =[]
    population_density = data.Population_Density.tolist()
    new_population_density = [str(i).replace(',', '').replace('nan','0').split('/') for i in population_density] #replace commas with '' and nan with 0
    for i in new_population_density:
        population_density_numbers.append(i[0])
    population_density_numbers = [float(i) for i in population_density_numbers] # turns strings into int

    x_pos = [i for i, _ in enumerate(cities)]

    plt.bar(x_pos, population_density_numbers, color='green')
    plt.xlabel("Cities")
    plt.ylabel("Population Density")
    plt.title("Population Densities of Various Cities")

    plt.xticks(x_pos, cities)

    plt.show()


