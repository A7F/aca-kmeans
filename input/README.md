## Input datasets
3 types of datasets available: points, blobs, iris. The first two are marked with number of points, but while the 
points dataset come with random points, cluster data are not given. Blob dataset instead also features the number of 
clusters. The latest dataset, iris, comes from [this website](https://archive.ics.uci.edu/ml/datasets/iris) and is 
known to have 150 points and 3 clusters as optimal choice.

as you may notice, file names have a standard formatting according to the dataset, number of points and number of 
clusters with the only exception to iris dataset because it's known data with known points and clusters:

| Dataset Name | file format | Points | Clusters | Data distribution | Script |
| ------------ | ----------- | ------ | -------- | ----------------- | ------ |
| points | `{points}points.txt` | {points} | {clusters} | random | make-points.py |
| blobs | `{points}-{clusters}-blob.txt` | {points} | {clusters} | gaussian | make-blobs.py |
| iris | `iris.txt` | 150 | 3 | correlation | pre-made dataset |

Each txt file simply carries a set of 2D cartesian coordinates X and Y representing a point with a signle space as 
separator, as follows:
```
5.3 -5
62 5.12
50.2 96
-86 -54.11
-63 44
5.4 6.9
-47.4 -11.1
-81 50
-78 10.01
-54 100
```