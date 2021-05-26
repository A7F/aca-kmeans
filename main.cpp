#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ctime>
#include <cmath>
#include "point.h"
#include "cluster.h"

using namespace std;

// define how many clusters of points we want and the total number of points
const int num_clusters = 3;
const int num_points = 50;

// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";


// defining data and functions
int load_dataset();
int init_clusters();
double distance(Point point, Cluster cluster);
void compute_distance();
Point points[num_points];
Cluster clusters[num_clusters];

int main(){
    srand(time(NULL));
    int tot_points = load_dataset();
    cout << "total points loaded: " << tot_points << endl;
    int tot_clusters = init_clusters();
    cout << "total clusters instantiated: " << tot_clusters << endl;
    for(int i=0; i<num_clusters; i++){
        clusters[i].print();
    }
    bool converged = false;

    // algorithm start. Compute distances between each point and centroids
    compute_distance();
    return 0;
}

// load dataset from file and store each point inside the array declared in the beginning
int load_dataset(){
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
    return i;
}

// initialize random pivoting elements as many as the number of clusters
int init_clusters(){
    int i=0;
    for(i; i<num_clusters; i++){
        int x = rand() % 100 + 1;
        int y = rand() % 100 + 1;
        Cluster cluster = Cluster(Point((int) x, (int) y));
        clusters[i] = cluster;
    }
    return i;
}

//compute the distance between all the points and centroids
void compute_distance(){
    for(int i=0; i<num_points; i++){
        double min_distance;
        int min_cluster_index;
        for(int j=0; j<num_clusters; j++){
            double tmp_distance = distance(points[i], clusters[j]);
            if(tmp_distance<min_distance){
                min_distance = tmp_distance;
                min_cluster_index = j;
            }
        }
        points[i].set_cluster(min_cluster_index);
        clusters[min_cluster_index].update_centroid(points[i]);
    }
}

// compute the distance between two 2D points (pythagorean theorem)
double distance(Point point, Cluster cluster){
    double d = sqrt(pow(point.get_x() - cluster.get_pivot().get_x(),2) +
                    pow(point.get_y() - cluster.get_pivot().get_y(), 2));
    return d;
}