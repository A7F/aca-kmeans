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
