from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import time


num_points = 10000
num_clusters = 4

start = time.time()


class Datasets:
    def __init__(self, points, clusters):
        self._points = points
        self._clusters = clusters
        self.POINTS = {"path": f"../input/{self._points}points.txt", "name": "points"}
        self.BLOBS = {"path": f"../input/{self._points}-{self._clusters}-blob.txt", "name": "blobs"}
        self.IRIS = {"path": "../input/iris.txt", "name": "iris"}

    def get_data(self, path):
        data = []
        with open(path, "r") as fin:
            lines = fin.readlines()
            for line in lines:
                x = float(line.split(" ")[0])
                y = float(line.split(" ")[1])
                data.append([x, y])
        return np.array(data)


ds = Datasets(num_points, num_clusters)
sel = ds.POINTS
raw_dataset = ds.get_data(sel["path"])

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("sk-learn K-Means Python clustering")
ax1.set_title("Initial dataset")
ax1.set_xlabel("x coordinate")
ax1.set_ylabel("y coordinate")
ax1.scatter(raw_dataset[:, 0], raw_dataset[:, 1], s=10)
ax2.set_title("Clustered dataset")
ax2.set_xlabel("x coordinate")
ax2.set_ylabel("y coordinate")

start_kmeans = time.time()
# kmeans in sklearn uses all threads by default with openmp (cython). Set env variable OMP_NUM_THREADS!!!
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(raw_dataset)
end_kmeans = time.time()
end = time.time()

wall_time = round(end - start, 5)
kmeans_time = round(end_kmeans - start_kmeans, 5)
print(f"code took {wall_time} sec from start to finish while kmeans alone took {kmeans_time} sec")
# LOG RUN TIMINGS
# timestamp,execution (s/p),language (p/c),dataset type,no. of points,no. of clusters,threads,no. of iterations,wall time,kmeans time
with open("../output/runs.csv", "a+") as stats:
    stats.write(f"{int(time.time())},{'s'},{'p'},{sel['name']},{num_points},{num_clusters},{1},{kmeans.n_iter_},{wall_time},{kmeans_time}\n")

ax2.scatter(raw_dataset[:, 0], raw_dataset[:, 1], s=10, c=kmeans.labels_)
ax2.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=90, marker="*", c="red")
plt.show()
