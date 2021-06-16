import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTANT: this file plots the results for the experiment 6 which is the one with different threads and points.
# So if you want to do such experiment, make sure your csv file is named "runs-exp6.csv".

dataset = "points"
num_points = [50000, 100000, 150000, 200000, 300000]
num_clusters = 10
tot_threads = [1, 4, 6, 8, 12]

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp6.csv", header=None, names=names)


plot = []
kmeans_weights = []
speedups = []

fig, ax = plt.subplots(1, 1)

for n_procs in tot_threads:
    plot = []
    kmeans_weights = []
    speedups = []

    for pts in num_points:
        df = data[(data["points"] == pts)]
        tmp = df[(data["threads"] == n_procs)]
        st = df[(data["threads"] == 1)]
        st = st["kmeans time"].mean()
        iters = df["iterations"].mean()
        mean = tmp["kmeans time"].mean()/iters
        if not np.isnan(mean):
            kmeans_weight = tmp["kmeans time"].mean() / (tmp["kmeans time"].mean() + tmp["serial time"].mean())
            total_time = tmp["kmeans time"].mean() + tmp["serial time"].mean()
            speedups.append([n_procs, round(st/total_time, 3)])
            kmeans_weights.append([n_procs, round(kmeans_weight, 2)])
            plot.append([pts, round(mean, 4)])

    ax.set_title("time for unitary kmeans iteration")
    ax.set_xlabel("points")
    ax.set_ylabel("kmeans iteration time (s)")
    ax.plot(*zip(*plot), label=f"{n_procs} CPU")

plt.legend()
plt.tight_layout()
plt.savefig("../plots/threads-compare.svg")
plt.show()
