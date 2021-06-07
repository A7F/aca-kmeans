# this small script generates the iris dataset for better cluster testing
# if you're curious, go look at https://archive.ics.uci.edu/ml/datasets/iris

import matplotlib.pyplot as plt
import numpy as np


class Iris:
    SEPAL_LENGTH = 0
    SEPAL_WIDTH = 1
    PETAL_LENGTH = 2
    PETAL_WIDTH = 3
    LABEL = 4


x = []
y = []
ground_truth = []

with open("../input/iris.data", "r") as fin:
    lines = fin.readlines()

with open("../input/iris.txt", "w") as fout:
    for line in lines:
        data = line.rstrip("\n").split(",")
        if len(data) == 1:
            continue
        x_coord = float(data[Iris.PETAL_LENGTH])
        y_coord = float(data[Iris.PETAL_WIDTH])
        x.append(x_coord)
        y.append(y_coord)
        gt = 0 if data[Iris.LABEL] == "Iris-setosa" else 1 if data[Iris.LABEL] == "Iris-versicolor" else 2
        ground_truth.append(gt)
        fout.write(f"{x_coord} {y_coord}\n")

plt.title("Iris dataset ground truth")
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.scatter(x, y, c=ground_truth)
plt.tight_layout()
plt.savefig("../plots/iris-groundtruth.svg", format="svg")
plt.show()
