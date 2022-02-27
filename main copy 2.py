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

