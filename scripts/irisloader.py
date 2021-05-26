# this small script generates the iris dataset for better cluster testing
# if you're curious, go look at https://archive.ics.uci.edu/ml/datasets/iris

import matplotlib.pyplot as plt


class Iris:
    SEPAL_LENGTH = 0
    SEPAL_WIDTH = 1
    PETAL_LENGTH = 2
    PETAL_WIDTH = 3


points = []

with open("../input/iris.data", "r") as fin:
    lines = fin.readlines()

with open("../input/iris.txt", "w") as fout:
    for line in lines:
        data = line.split(",")
        if len(data) == 1:
            continue
        x = data[Iris.PETAL_LENGTH]
        y = data[Iris.PETAL_WIDTH]
        points.append((x, y))
        fout.write(f"{x} {y}\n")

plt.scatter(*zip(*points))
plt.show()
