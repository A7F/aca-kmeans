## Input datasets
3 types of datasets available: points, bolbs, iris. The first two are marked with number of points, but while the 
points dataset come with random points, cluster data are not given. Blob dataset instead also features the number of 
clusters. The latest dataset, iris, comes from [this website](https://archive.ics.uci.edu/ml/datasets/iris) and is 
known to have 150 points and 3 clusters as optimal choice.

| File | Dataset name | Points | Clusters | Data distribution | Script |
| ------- | -------| ------ | -------- | ----------------- | ------ |
| 50points | points | 50 | unknown | random | make-points.py |
| 100points | points | 100 | unknown | random | make-points.py |
| 150points | points | 150 | unknown | random | make-points.py |
| 300points | points | 300 | unknown | random | make-points.py |
| 500points | points | 500 | unknown | random | make-points.py |
| 500-2-blob | blobs | 500 | 2 | gaussian | sklearn-blobs.py |
| 500-3-blob | blobs | 500 | 3 | gaussian | sklearn-blobs.py |
| 500-4-blob | blobs | 500 | 4 | gaussian | sklearn-blobs.py |
| 1000-2-blob | blobs | 1000 | 2 | gaussian | sklearn-blobs.py |
| 1000-3-blob | blobs | 1000 | 3 | gaussian | sklearn-blobs.py |
| 1000-4-blob | blobs | 1000 | 4 | gaussian | sklearn-blobs.py |
| iris | iris | 150 | 3 | correlation | no script |

as you may notice, file names have a standard formatting according to the dataset, number of points and number of 
clusters with the only exception to iris dataset because it's known data with known points and clusters:

| Dataset Name | file format |
| ------------ | ----------- |
| points | {points}points.txt |
| blobs | {points}-{clusters}-blob.txt |

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