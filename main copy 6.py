import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
  
setup()


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = [] #Empty List
    for i in range(0,1000):
        # Calling the function random_set_of_mean and the result is stored inside set_of_means
        set_of_means= random_set_of_mean(100) #1000 values are stored inside set_of_means
        mean_list.append(set_of_means)#adding 1000 values to list

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation() #Calling function


