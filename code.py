import pandas as bear
import statistics as stats
import random
import csv
import plotly.figure_factory as ff

df = bear.read_csv("medium_data.csv")

# SOME DATA TYPE NAMES:
# claps
# responses (not working for some reason)
# reading_time
data_name = str(input("Enter the data type name: "))
data = df[data_name].tolist()
population_mean = stats.mean(data)
#print(population_mean)

#fig = ff.create_distplot([data], [""], show_hist=False)
#fig.show()

def sample_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean_sample = stats.mean(dataset)

    return mean_sample

def plot_graph(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], [f"Average of Sample Means of {data_name}"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = sample_mean(30)
        mean_list.append(set_of_mean)
    plot_graph(mean_list)
    mean_list_mean = stats.mean(mean_list)
    print(f"Mean of Sample Means is {mean_list_mean}")
    print(f"Population Mean is {population_mean}")

setup()
