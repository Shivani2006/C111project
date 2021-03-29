import csv
import pandas as pd 
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random


df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

print("mean of population: ", mean)
print("median of population: ", median)
print("mode of population: ", mode)
print("standard deviation of population: ", std_dev)

def sampling(ppopulation_data):
    sample_data = []
    for i in range(0,100):
        random_index = random.randint(0,100)
        value = ppopulation_data[random_index]
        sample_data.append(value)
    mean = statistics.mean(sample_data)
    std  = statistics.stdev(sample_data)
    return mean, std

mean_list=[]
for i in range(0,1000):
    sample_mean,sample_std=sampling(data)
    mean_list.append(sample_mean)
avg = statistics.mean(mean_list)
sd  = statistics.stdev(mean_list)
print("sampling mean: ",avg," , sampling std_dev: ",sd)

df1 = pd.read_csv("data1.csv")
data1 = df["Math_score"].tolist()

mean_grp1 = statistics.mean(data1)
std_dev_grp1= statistics.stdev(data1)

df2 = pd.read_csv("data2.csv")
data2 = df["Math_score"].tolist()

mean_grp2 = statistics.mean(data2)
std_dev_grp2= statistics.stdev(data2)

df3 = pd.read_csv("data3.csv")
data3 = df["Math_score"].tolist()

mean_grp3= statistics.mean(data3)
std_dev_grp3= statistics.stdev(data3)

fig = ff.create_distplot([mean_list], ["Math Scores"], show_hist=False)
fig.add_trace(go.Scatter(x = [avg,avg], y= [0, 0.17], mode="lines", name = "MEAN"))

fig.add_trace(go.Scatter(x = [mean_grp1, mean_grp1], y= [0, 0.17], mode="lines", name = "MEAN of grp 1"))
fig.add_trace(go.Scatter(x = [mean_grp2, mean_grp2], y= [0, 0.17], mode="lines", name = "MEAN of grp 2"))
fig.add_trace(go.Scatter(x = [mean_grp3, mean_grp3], y= [0, 0.17], mode="lines", name = "MEAN of grp 3"))
fig.show()