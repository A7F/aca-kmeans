import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

# IMPORTANT: this file plots the results for the experiment 3 which is the comparison between serial python and serial
# cpp kmeans. So if you want to do such experiment, make sure your csv file is named "runs-exp3.csv".

dataset = "points"
num_points = [10000, 50000, 100000, 150000, 200000, 300000]
num_clusters = 10
threads = 1

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp3.csv", header=None, names=names)


fig, ax = plt.subplots(1, 2)
fig.suptitle(f"C++ vs Python serial code, {num_clusters} clusters, capped iterations to python")

dfs = [data[(data["lang"] == "c")], data[(data["lang"] == "p")]]

for i, df in enumerate(dfs):
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

    ax[0].set_title("average kmeans time per iteration")
    ax[0].set_xlabel("number of points")
    ax[0].set_ylabel("iteration time (avg sec.)")
    ax[0].plot(*zip(*plot), label=f"{'C++' if i==0 else 'Python'}")
    ax[0].legend()

speedups = []
for points in num_points:
    c_data = dfs[0][dfs[0]["points"] == points]
    p_data = dfs[1][dfs[1]["points"] == points]
    c_tot_time = c_data["kmeans time"].mean() + c_data["serial time"].mean()
    p_tot_time = p_data["kmeans time"].mean() + p_data["serial time"].mean()
    speedup = round(c_tot_time/p_tot_time, 2)
    speedups.append([points, speedup])


ax[1].set_title("Average C++ speedups against Python")
ax[1].set_xlabel("number of points")
ax[1].set_ylabel("Speedup factor")
x_new = np.linspace(min(num_points), max(num_points), 2)
speedups = np.array(speedups)
a_BSpline = interpolate.make_interp_spline(speedups[:, 0], speedups[:, 1], k=3)
y_new = a_BSpline(x_new)
ax[1].plot(x_new, y_new, label="C++")
ax[1].legend()

plt.tight_layout()
plt.show()
