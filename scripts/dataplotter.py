# output file to process is in the format X Y CATEGORY
# this file processes the output of the algorithm and displays it in a scatter plot

import matplotlib.pyplot as plt
import numpy as np

with open("../output/res.txt", "r") as fin:
    lines = fin.readlines()

num_clusters = int(lines[0])
print(f"found {num_clusters} clusters.")
x_coord = []
y_coord = []
label = []

pivots = []
for line in lines[1:num_clusters+1]:
    data = line.split(" ")
    pivots.append((float(data[0]), float(data[1])))

for line in lines[1:]:
    data = line.split(" ")
    x_coord.append(float(data[0]))
    y_coord.append(float(data[1]))
    label.append(float(data[2]))

categories = np.array(label)

plt.title(f"K-means output result for {len(label)-num_clusters} points, {num_clusters} clusters")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.scatter(x_coord, y_coord, c=label)
plt.scatter(*zip(*pivots), s=90, marker="*", c="red")
plt.show()
