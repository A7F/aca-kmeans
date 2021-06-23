<h1 align="center">K-Means clustering</h1>
<h5 align="center">Luca Todaro and Rasha Zieni, University of Pavia</h5>
this repository contains the code for our Advanced Computer Architecture project work: an implementation of serial and 
parallel k-means clustering algorithm, written in C++. Oh and by the way, we got A+. :D

## Project description
we are running the kmeans algorithm both in C++ (our own serial and parallel implementation) as well as in Python using 
the serial implementation of Scikit-Learn. The aim of the project is to demonstrate the performance 
increase when switching from serial to parallel programming, plus we decided to spice the things up comparing how fast 
the serial C++ implementation is against the one in Python from a well-known library (so we assume it's a state of 
art implementation!). 

Because the algorithm is intrinsically non-deterministic, we decided to start the algorithm with pre-defined datasets to 
decrease variance between experiments. Please check the folder input for more infos about the datasets we used.

### Run the code on Google Cloud Platform
We included an easy script (that is, `prepare-project.sh`) that helps configuring the environment on your virtual machine. 
All you need to do is to install git with

`sudo apt-get install git`

and then clone this repo:

`git clone https://github.com/A7F/aca-kmeans.git`

move to the newly created folder with `cd aca-kmeans` and assign run permissions to the script `prepare-project.sh` with

`sudo chmod 777 ./prepare-project.sh`

Please remember to set the correct working directory inside the script you want to run first! For example, if you want to run 
the serial script, paste your path inside the variable `base_dir`. After that, the bash script we provided automatically 
builds the project and prepares the runnable file in the same directory, so all you need to do is to call `./aca_kmeans`.

## Some useful resources...
follows a small section of useful links and resources to keep in hand, you know... <i>just in case</i>...

[project presentation](./resources/project_presentation.pdf)
[project report](./resources/project_report.pdf)

### Course links
[aca project work page](http://www-5.unipv.it/mferretti/cdol/aca/Examination%20and%20project%20work.htm) and 
[course index](http://www-5.unipv.it/mferretti/cdol/aca/index.htm)

