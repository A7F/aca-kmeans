from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import time


num_points = 150
num_clusters = 5


class Datasets:
    def __init__(self, points, clusters):
        self._points = points
        self._clusters = clusters
        self.POINTS = f"../input/{self._points}points.txt"
        self.BLOBS = f"../input/{self._points}-{self._clusters}-blob.txt"
        self.IRIS = f"../input/iris.txt"

    def get_data(self, path):
        data = []
        with open(path, "r") as fin:
            lines = fin.readlines()
            for line in lines:
                x = float(line.split(" ")[0])
                y = float(line.split(" ")[1])
                data.append([x, y])
        return np.array(data)


start = time.time()
ds = Datasets(num_points, num_clusters)
raw_dataset = ds.get_data(ds.IRIS)

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("sk-learn K-Means Python clustering")
ax1.set_title("Initial dataset")
ax1.set_xlabel("x coordinate")
ax1.set_ylabel("y coordinate")
ax1.scatter(raw_dataset[:, 0], raw_dataset[:, 1])
ax2.set_title("Clustered dataset")
ax2.set_xlabel("x coordinate")
ax2.set_ylabel("y coordinate")

kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(raw_dataset)
end = time.time()
print(f"code took {round(end - start, 5)} seconds from start to finish")
ax2.scatter(raw_dataset[:, 0], raw_dataset[:, 1], c=kmeans.labels_)
ax2.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=90, marker="*", c="red")
plt.show()