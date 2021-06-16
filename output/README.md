## Output data
there are two files here: `res.txt` and `runs.txt`. The first acts as a middlemen to make the data available to the python 
plotting script, while the latter stores all the runs for both CPP and Python k-means implementations. 

### result file
First row is a single number that specifies how many clusters to expect; in all the following rows there are 3 numbers 
separated by 1 space: x and y coordinates, and a number that represents cluster assignation from k-means algorithm. 
This is how it should look like:
```
2
7.7099 0.0968748 0
-9.30275 4.62383 1
-10.3098 5.98627 1
-9.76686 4.31869 0
-8.6281 5.27513 1
...
```

This file gets overwritten at each new run, so if you want to preserve its content, please remember to rename it to 
something different from `res.txt`

### runs file
whenever a k-means implementation run, regardless of its programming language, the output stats are stored in this file. 
It is accessed with permission "append" and it never gets erased, but it is possible to start logging into a new file 
by renominating the current one to something different from `res.txt`. 
```
1622320725,s,p,blobs,50000,2,1,12,0.34308,0.10472
1622320744,p,c,blobs,30000,2,6,123,0.28324,0.0748
1622320751,p,c,blobs,30000,2,2,3,0.27526,0.07679
...
```
This is a CSV file, basically. On each line:
`linux epoch timestamp,execution (s/p),language (p/c),dataset type,no. of points,no. of clusters,threads,no. of iterations,wall time,kmeans time`
where execution can assume values s (serial) or p (parallel); language can be either p (python) or c (C++).

### description of experiments
runs-exp1: hard capped max iterations number so that all the types of codes (serial and parallel from 1 to 12 threads) 
do the same number of iterations. Fixed number of points and clusters. Use the python script `exp1-stats.py`

runs-exp2: no hard cap on iteration number, the algorithm is just free to converge in how many iterations are needed.
Fixed number of points and clusters, same as runs-exp1. Use the file `exp2-stats.py`. 

runs-exp3: a comparison with serial Python and serial C++ varying the number of points but with fixed number of clusters.
Iterations are capped in cpp code according to those needed in Python to make a fair comparison

runs-exp4: running serial code c++ and with fixed number of points but varying the clusters. We notice an increase 
in the average kmeans time to complete a single iteration, as expected.

runs-exp5: serial cpp code, we fix the number of clusters and we vary the number of points. Goal is to see if there are any 
differences with exp4.

runs-exp6: performance comparison between the increase in amount of cores and the amount of data points, to check how well 
the overall parallel implementation scales compared to the serial one.

gcp-parallel: measures on gcp varying the number of core count and data points as input, but fixed number of clusters to 10. 
It also includes runs with the serial script and the iterations are not fixed in all the combinations of cores, points and clusters.
