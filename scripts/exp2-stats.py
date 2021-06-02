import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

# IMPORTANT: this file plots the results for the experiment 2 which is the one without hard-capped number of iterations.
# So if you want to do such experiment, make sure your csv file is named "runs-exp2.csv".

dataset = "points"
num_points = 300000
num_clusters = 10
threads = list(range(1, 13))
tot_threads = 12

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs-exp2.csv", header=None, names=names)


plot = []
kmeans_weights = []
speedups = []
iterations = []

fig, ax = plt.subplots(2, 2)
fig.suptitle(f"C++ run stats for {num_points} points and {num_clusters} clusters")

st = data[(data["threads"] == 1) & (data["lang"] == "c")]

for thread in threads:
    df = data[(data["threads"] == thread) & (data["dataset"] == dataset) & (data["lang"] == "c")]

    std = st["kmeans time"].mean() + st["serial time"].mean()
    iters = df["iterations"].mean()
    iterations.append([thread, iters])
    mean = df["kmeans time"].mean()/iters
    if not np.isnan(mean):
        kmeans_weight = df["kmeans time"].mean() / (df["kmeans time"].mean() + df["serial time"].mean())
        total_time = df["kmeans time"].mean() + df["serial time"].mean()
        speedups.append([thread, round(std/total_time, 3)])
        kmeans_weights.append([thread, round(kmeans_weight, 2)])
        plot.append([thread, round(mean, 4)])

ax[0][0].set_title("average iterations to converge")
ax[0][0].set_xlabel("threads count")
ax[0][0].set_ylabel("iterations")
ax[0][0].plot(*zip(*iterations))

ax[0][1].set_title("kmeans relevance over total execution time")
ax[0][1].set_xlabel("threads count")
ax[0][1].set_ylabel("P factor")
ax[0][1].plot(*zip(*kmeans_weights))

ax[1][0].set_title("Average speedups")
ax[1][0].set_xlabel("threads count")
ax[1][0].set_ylabel("Speedup factor")
ax[1][0].plot(*zip(*speedups))

ax[1][1].set_title("average kmeans time per iteration")
ax[1][1].set_xlabel("threads count")
ax[1][1].set_ylabel("iterations (avg)")
x_new = np.linspace(1, 12, 100)
plot = np.array(plot)
a_BSpline = interpolate.make_interp_spline(plot[:, 0], plot[:, 1], k=3)
y_new = a_BSpline(x_new)
ax[1][1].plot(x_new, y_new, alpha=0.6, linewidth=1.2, linestyle="dashed")
ax[1][1].plot(*zip(*plot))

plt.tight_layout()
plt.show()
