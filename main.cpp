#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "point.h"
#include "cluster.h"

using namespace std;

// define how many clusters of points we want and the total number of points
const int num_clusters = 3;
const int num_points = 50;

// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";


// defining data and functions
void load_dataset();
Point points[num_points];
Cluster clusters[num_clusters];

int main(){
    load_dataset();
    return 0;
}

void load_dataset(){
    std::stringstream ss;
    ss << base_dir << "input\\" << num_points << "points-1.txt";
    string filepath = ss.str();
    ifstream infile(filepath);
    if(!infile){
        cerr << "Could not open file. Maybe the number of points set is wrong?" << std::endl;
    }
    int x, y, i=0;
    while(infile >> x >> y){
        Point point((int) x, (int) y);
        points[i] = point;
        i++;
    }
}