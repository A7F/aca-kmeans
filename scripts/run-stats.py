import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = "points"
num_points = 300000
num_clusters = 10
num_threads = 6
num_iters = 50

names = ["timestamp", "lang", "type", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs.csv", header=None, names=names)
df = data[(data["iterations"] == num_iters) & (data["dataset"] == dataset)]
# print(df)

plot = []
for n_procs in range(0,13):
    tmp = df[(data["threads"] == n_procs)]
    mean = tmp["kmeans time"].mean()/num_iters
    if not np.isnan(mean):
        plot.append([n_procs, round(mean, 4)])

plt.title(f"iter time for {num_points} points and {num_clusters} clusters")
plt.xlabel("threads count")
plt.ylabel("kmeans iteration time (s)")
plt.plot(*zip(*plot))
plt.show()