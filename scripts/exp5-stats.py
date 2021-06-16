import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

# IMPORTANT: this file plots the results for the experiment 3 which is the cpp kmeans serial time varying number of points.
# fixed clusters. So if you want to do such experiment, make sure your csv file is named "runs-exp5.csv".

dataset = "points"
num_points = [10000, 50000, 100000, 150000, 200000, 300000]
num_clusters = 10
threads = 1

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp5.csv", header=None, names=names)

fig, ax = plt.subplots(1, 1)
ax.set_title(f"Serial iteration time, {num_clusters} clusters")

df = data[(data["lang"] == "c")]


plot = []
speedups = []
for points in num_points:
    n_df = df[df["points"] == points]
    std = n_df["kmeans time"].mean() + n_df["serial time"].mean()
    iters = n_df["iterations"].mean()
    mean = n_df["kmeans time"].mean()/iters
    kmeans_weight = n_df["kmeans time"].mean() / (n_df["kmeans time"].mean() + n_df["serial time"].mean())
    total_time = n_df["kmeans time"].mean() + n_df["serial time"].mean()
    speedups.append([points, round(std/total_time, 3)])
    plot.append([points, round(mean, 4)])

ax.set_xlabel("points")
ax.set_ylabel("avg. iteration time in seconds")
ax.plot(*zip(*plot))


plt.tight_layout()
plt.savefig("../plots/serial-points-cpp.svg")
plt.show()
