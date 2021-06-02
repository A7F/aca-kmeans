import os.path
import random
import numpy as np
import matplotlib.pyplot as plt

# parameters to consider when generating the file
tot_points = 200000
min_val = -10000
max_val = 10000
filepath = f"../input/{tot_points}points.txt"

points = []

# search for target file.
# If exists, just print the points stored.
# If does not exists, generates a new one with parameters specified above
if os.path.isfile(filepath):
    print("file points already exists. Delete or rename it if you want to generate a new one.")
    with open(filepath, "r") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.strip()
            x, y = line.split(" ")
            if (float(x), float(y)) not in points:
                points.append((float(x), float(y)))
else:
    with open(filepath, "w") as fin:
        for i in range(tot_points):
            while True:
                x = round(random.uniform(min_val, max_val), 3)
                y = round(random.uniform(min_val, max_val), 3)
                if (x, y) not in points:
                    points.append((x, y))
                    fin.write(f"{x} {y}\n")
                    break

# plt.scatter(*zip(*points))
# plt.show()
