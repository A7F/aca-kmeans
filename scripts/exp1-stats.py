import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTANT: this file plots the results for the experiment 1 which is the one with hard-capped number of iterations.
# So if you want to do such experiment, make sure your csv file is named "runs-exp1.csv".

dataset = "points"
num_points = 300000
num_clusters = 10
num_iters = [10, 30, 50]
tot_threads = 12

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp1.csv", header=None, names=names)


plot = []
kmeans_weights = []
speedups = []

fig, ax = plt.subplots(2, 2)
fig.suptitle(f"C++ run stats for {num_points} points and {num_clusters} clusters")

for iters in num_iters:
    df = data[(data["iterations"] == iters) & (data["dataset"] == dataset)]
    plot = []
    kmeans_weights = []
    speedups = []

    for n_procs in range(0, tot_threads+1):
        tmp = df[(data["threads"] == n_procs) & (data["lang"] == "c")]
        st = df[(data["threads"] == 1) & (data["lang"] == "c")]
        st = st["kmeans time"].mean() + st["serial time"].mean()
        mean = tmp["kmeans time"].mean()/iters
        if not np.isnan(mean):
            kmeans_weight = tmp["kmeans time"].mean() / (tmp["kmeans time"].mean() + tmp["serial time"].mean())
            total_time = tmp["kmeans time"].mean() + tmp["serial time"].mean()
            speedups.append([n_procs, round(st/total_time, 3)])
            kmeans_weights.append([n_procs, round(kmeans_weight, 2)])
            plot.append([n_procs, round(mean, 4)])

    ax[0][0].set_title("time for unitary kmeans iteration")
    ax[0][0].set_xlabel("threads count")
    ax[0][0].set_ylabel("kmeans iteration time (s)")
    ax[0][0].plot(*zip(*plot), label=f"{iters} iters")
    ax[0][0].legend()

    ax[0][1].set_title("kmeans relevance over total execution time")
    ax[0][1].set_xlabel("threads count")
    ax[0][1].set_ylabel("P factor")
    ax[0][1].plot(*zip(*kmeans_weights), label=f"{iters} iters")
    ax[0][1].legend()

    ax[1][0].set_title("Speedups")
    ax[1][0].set_xlabel("threads count")
    ax[1][0].set_ylabel("Speedup factor")
    ax[1][0].plot(*zip(*speedups), label=f"{iters} iters")
    ax[1][0].legend()

    counts = df["threads"].value_counts()
    ax[1][1].set_title("Number of runs")
    ax[1][1].set_xlabel("threads count")
    ax[1][1].set_ylabel("total runs gathered")
    ax[1][1].hist(counts.index, weights=counts.values, bins=12, alpha=0.5, label=f"{iters} iters")
    ax[1][1].legend()

plt.tight_layout()
plt.show()
