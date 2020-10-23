import matplotlib.pyplot as plt
import pandas


def graphIt():
    # colnames = ['City', 'Estimated_Population']
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