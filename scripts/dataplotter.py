# output file to process is in the format X Y CATEGORY
# this file processes the output of the algorithm and displays it in a scatter plot

import matplotlib.pyplot as plt
import numpy as np

with open("../output/res.txt", "r") as fin:
    lines = fin.readlines()

x_coord = []
y_coord = []
label = []

for line in lines:
    data = line.split(" ")
    x_coord.append(int(data[0]))
    y_coord.append(int(data[1]))
    label.append(int(data[2]))

categories = np.array(label)

plt.title(f"K-means output result for {len(label)} points")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.scatter(x_coord, y_coord, c=label)
plt.show()
