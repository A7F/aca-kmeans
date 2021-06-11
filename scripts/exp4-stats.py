import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# IMPORTANT: this file plots the results for the experiment 4 which is the one with fixed number of points, serial code.
# So if you want to do such experiment, make sure your csv file is named "runs-exp4R.csv" and "runs-exp4L.csv".

dataset = "points"
num_points = 300000
num_clusters = [2, 4, 8, 10]

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp4R.csv", header=None, names=names)

x = []
y = []

for cluster in num_clusters:
    df = data[(data["clusters"] == cluster)]
    avg_tot_time = df["kmeans time"].mean()
    avg_iters = df["iterations"].mean()
    avg_iter_time = round(avg_tot_time/avg_iters, 2)
    x.append(cluster)
    y.append(avg_iter_time)

plt.plot(x, y, label="i5 7500U")

data = pd.read_csv("../output/runs-exp4L.csv", header=None, names=names)

x = []
y = []

for cluster in num_clusters:
    df = data[(data["clusters"] == cluster)]
    avg_tot_time = df["kmeans time"].mean()
    avg_iters = df["iterations"].mean()
    avg_iter_time = round(avg_tot_time/avg_iters, 2)
    x.append(cluster)
    y.append(avg_iter_time)

plt.title("Serial iteration time, 100000 points")
plt.xlabel("clusters")
plt.ylabel("avg. iteration time")
plt.plot(x, y, label="i7 10710U")
plt.legend()

plt.tight_layout()
plt.savefig("../plots/serial-cpp.svg")
plt.show()
