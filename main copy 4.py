# START FROM THE END

import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#code to find mean and std deviation of 100 data points
dataset = []
for i in range(0, 100):
    random_index= random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of sample:- ",mean)
print("std_deviation of sample:- ",std_deviation)


##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = [] #Empty List
    for i in range(0, counter): # 0 to 100
    # We are generating a random num b/w 0 and len(data-1) as we are starting from 0
    # And the generated number we are considering as index and storing it in random_index
        random_index= random.randint(0,len(data)-1)
         # ex : random_index is 126, data[126]=40
        value = data[random_index]
        # 40 will be stored inside value
        dataset.append(value) #adding all the values to the list
    mean = statistics.mean(dataset)
    return mean  #We are giving the mean value for the function setup()
    #It is done 1000 times, 1000 mean values will go to setup

# #function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list #All the 100 values are stored in df
    mean = statistics.mean(df) #Finding the mean for all 1000 elements
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()


# # Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = [] #Empty List
    for i in range(0,1000):
        # Calling the function random_set_of_mean and the result is stored inside set_of_means
        set_of_means= random_set_of_mean(100) #1000 values are stored inside set_of_means
        # print(set_of_means)
        mean_list.append(set_of_means) #adding 1000 values to list
    show_fig(mean_list)  #Calling function
    

# We are calling the setup function 
setup()
