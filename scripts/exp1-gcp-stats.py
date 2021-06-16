import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTANT: this file plots the results for the experiment 1 which is the one with hard-capped number of iterations.
# So if you want to do such experiment, make sure your csv file is named "runs-exp1.csv".

dataset = "points"
num_points = [10000, 50000, 100000, 150000, 200000, 300000]
num_clusters = 10
tot_threads = 12

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/gcp-serial.csv", header=None, names=names)

plot = []
for pts in num_points:
    df = data[(data["points"] == pts)]
    avg_iters = df["iterations"].mean()
    avg_time = df["kmeans time"].mean()
    avg_time_iter = round(avg_time/avg_iters, 2)
    plot.append([pts, avg_time_iter])

plt.title("GCP average serial time")
plt.xlabel("number of points")
plt.ylabel("time in seconds")
plt.plot(*zip(*plot))
plt.show()
