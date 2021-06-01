import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = "points"
num_points = 300000
num_clusters = 10
num_iters = 50
tot_threads = 12

names = ["timestamp", "type", "lang", "dataset", "points", "clusters", "threads", "iterations", "serial time", "kmeans time"]
data = pd.read_csv("../output/runs.csv", header=None, names=names)
df = data[(data["iterations"] == num_iters) & (data["dataset"] == dataset)]
print(df)

plot = []
kmeans_weights = []
speedups = []

for n_procs in range(0, tot_threads+1):
    tmp = df[(data["threads"] == n_procs) & (data["lang"] == "c")]
    st = df[(data["threads"] == 1) & (data["lang"] == "c")]
    st = st["kmeans time"].mean() + st["serial time"].mean()
    mean = tmp["kmeans time"].mean()/num_iters
    if not np.isnan(mean):
        kmeans_weight = tmp["kmeans time"].mean() / (tmp["kmeans time"].mean() + tmp["serial time"].mean())
        total_time = tmp["kmeans time"].mean() + tmp["serial time"].mean()
        speedups.append([n_procs, round(st/total_time, 3)])
        kmeans_weights.append([n_procs, round(kmeans_weight, 2)])
        plot.append([n_procs, round(mean, 4)])

fig, ax = plt.subplots(2, 2)

fig.suptitle(f"C++ run stats for {num_points} points and {num_clusters} clusters")
ax[0][0].set_title("time for unitary kmeans iteration")
ax[0][0].set_xlabel("threads count")
ax[0][0].set_ylabel("kmeans iteration time (s)")
ax[0][0].plot(*zip(*plot), label=f"{num_iters} iters")
ax[0][0].legend()

ax[0][1].set_title("kmeans relevance over total execution time")
ax[0][1].set_xlabel("threads count")
ax[0][1].set_ylabel("P factor")
ax[0][1].plot(*zip(*kmeans_weights), label=f"{num_iters} iters")
ax[0][1].legend()

ax[1][0].set_title("Speedups")
ax[1][0].set_xlabel("threads count")
ax[1][0].set_ylabel("Speedup factor")
ax[1][0].plot(*zip(*speedups), label=f"{num_iters} iters")
ax[1][0].legend()

plt.tight_layout()
plt.show()
