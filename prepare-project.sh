#!/bin/sh
apt-get install cmake -y
mkdir our_builds
cd our_builds
cmake ../../aca-kmeans
cmake --build .