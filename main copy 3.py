import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population mean:- ", population_mean)
print("std_deviation:- ", std_deviation)


#code to find mean and std deviation of 100 data points
dataset = []
for i in range(0, 100):
    # We are generating a random num b/w 0 and len of data, 
    # And the generated number we are considering as index and storing it in random_index
    random_index= random.randint(0,len(data))
    print(random_index)
    # ex : random_index is 126, data[126]=40
    value = data[random_index]
    # 40 will be stored inside value
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of sample:- ",mean)
print("std_deviation of sample:- ",std_deviation)







