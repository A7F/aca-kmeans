<h1 align="center">K-Means clustering</h1>
<h5 align="center">Luca Todaro and Rasha Zieni, University of Pavia</h5>
this repository contains the code for our Advanced Computer Architecture project work: an implementation of serial and 
parallel k-means clustering algorithm, written in C++.

## Project description
we are running the kmeans algorithm both in C++ (our own serial and parallel implementation) as well as in Python using 
the serial implementation of Scikit-Learn. The aim of the project is to demonstrate the performance 
increase when switching from serial to parallel programming, plus we decided to spice the things up comparing how fast 
the serial C++ implementation is against the one in Python from a well-known library (so we assume it's a state of 
art implementation!). 

Because the algorithm is intrinsically non-deterministic, we decided to start the algorithm with pre-defined datasets to 
decrease variance between experiments. Please check the folder input for more infos about the datasets we used.

## Some useful resources...
follows a small section of useful links and resources to keep in hand, you know... <i>just in case</i>...

### Course links
[aca project work page](http://www-5.unipv.it/mferretti/cdol/aca/Examination%20and%20project%20work.htm) and 
[course index](http://www-5.unipv.it/mferretti/cdol/aca/index.htm)

### K-Means resources in the wild...

[kmeans and parallelization - quick study](https://www.slideshare.net/ssuserf88631/parallel-kmeans-43373444)

[k-means in python, C++ and CUDA](http://www.goldsborough.me/c++/python/cuda/2017/09/10/20-32-46-exploring_k-means_in_python,_c++_and_cuda/)

[k-means in C++](https://reasonabledeviations.com/2019/10/02/k-means-in-cpp/#the-k-means-algorithm)

[k-means in C++ and OpenMP](https://github.com/arneish/parallel-k-means)

[another implementation in C++ and OpenMP](https://github.com/SestoAle/Parallel-K-Means)

[k-means with CUDA](https://github.com/serban/kmeans)

[parallelization of K-means serial using CUDA](https://arxiv.org/pdf/1908.02136.pdf)

[super awesome explanation of kmeans clustering (yes I know it's in italian...)](https://www.lorenzogovoni.com/algoritmo-k-means-cose-e-come-funziona/)

[another super useful explanation of the algorithm, but this time is in english](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)

[k-means implementation + report with openmp and c++](https://github.com/SestoAle/Parallel-K-Means)