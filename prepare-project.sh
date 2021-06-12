#!/bin/sh
apt-get install cmake -y
sudo apt-get install build-essential -y
mkdir our_builds
cd our_builds
cmake ../../aca-kmeans
cmake --build .
mv aca_kmeans ../