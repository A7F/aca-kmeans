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
const int num_clusters = 2;
const int num_points = 100;

// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";


// defining data and functions
int load_dataset();
int init_clusters();
double distance(Point point, Cluster cluster);
bool naive_kmeans();
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
    int iteration = 0;
    while(!converged){
        iteration++;
        // reset dimension for all the clusters before starting a new iteration
        for(int i=0; i<num_clusters; i++){
            clusters[i].set_dimension(0);
        }
        converged = naive_kmeans();
    }

    cout << endl << "======= results after convergence (" << iteration << " iters) =======" << endl;

    // print the clusters once the algorithm has converged
    for(int i=0; i<num_clusters; i++){
        clusters[i].print();
    }

    return 0;
}

// load dataset from file and store each point inside the array declared in the beginning
int load_dataset(){
    stringstream ss;
    ss << base_dir << "input\\" << num_points << "points-1.txt";
    // ss << base_dir << "input\\iris.txt";
    string filepath = ss.str();
    ifstream infile(filepath);
    if(!infile){
        cerr << "Could not open file. Maybe the number of points set is wrong?" << std::endl;
    }
    int x, y, i=0;
    while(infile >> x >> y){
        Point point((float) x, (float) y);
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
bool naive_kmeans(){
    bool has_converged = false;
    int updates = 0;
    for(int i=0; i<num_points; i++){
        double min_distance = 9999999;
        int min_cluster_index = 42;
        for(int j=0; j<num_clusters; j++){
            double tmp_distance = distance(points[i], clusters[j]);
            if(tmp_distance<min_distance){
                min_distance = tmp_distance;
                min_cluster_index = j;
            }
        }
        int old_cluster = points[i].get_cluster();
        if (old_cluster == min_cluster_index){
            has_converged = true;
        } else {
            updates++;
            points[i].set_cluster(min_cluster_index);
        }
        clusters[min_cluster_index].update_centroid(points[i]);
    }
    has_converged = (updates == 0);
    return has_converged;
}

// compute the distance between two 2D points (pythagorean theorem)
double distance(Point point, Cluster cluster){
    double d = sqrt(pow(point.get_x() - cluster.get_pivot().get_x(),2) +
                    pow(point.get_y() - cluster.get_pivot().get_y(), 2));
    return d;
}