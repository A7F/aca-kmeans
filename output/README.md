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

### runs file
whenever a k-means implementation run, regardless of its programming language, the output stats are stored in this file. 
It is accessed with permission "append" and it never gets erased, but it is possible to start logging into a new file 
by renominating the current one to something different than `res.txt`. 
```
1622320725,s,p,blobs,50000,2,1,12,0.34308,0.10472
1622320744,s,p,blobs,30000,2,6,123,0.28324,0.0748
1622320751,s,p,blobs,30000,2,2,3,0.27526,0.07679
...
```
This is a CSV file, basically. On each line:
`linux epoch timestamp,execution (s/p),language (p/c),dataset type,no. of points,no. of clusters,no. of iterations,wall time,kmeans time`
where execution can assume values s (serial) or p (parallel); language can be either p (python) or c (C++).