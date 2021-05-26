import os.path
import random
import matplotlib.pyplot as plt

# parameters to consider when generating the file
tot_points = 300
min_val = -100
max_val = 100
filepath = f"../input/{tot_points}points-1.txt"

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
            if (int(x), int(y)) not in points:
                points.append((int(x), int(y)))
else:
    with open(filepath, "w") as fin:
        for i in range(tot_points):
            x = random.randint(min_val, max_val)
            y = random.randint(min_val, max_val)
            if (x, y) not in points:
                points.append((x, y))
                fin.write(f"{x} {y}\n")

plt.scatter(*zip(*points))
plt.show()
