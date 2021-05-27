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
const int num_points = 150;

// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";


// defining data and functions
int load_dataset(bool iris_dataset);
int init_clusters();
double distance(Point point, Cluster cluster);
bool naive_kmeans();
void export_result();
Point points[num_points];
Cluster clusters[num_clusters];


int main(){
    srand(time(NULL));
    int tot_points = load_dataset(false);
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
        converged = naive_kmeans();
        // reset dimension for all the clusters before starting a new iteration
        for(int i=0; i<num_clusters; i++){
            clusters[i].update_centroid();
            clusters[i].empty_pivot();
        }
    }

    cout << endl << "======= results after convergence (" << iteration << " iters) =======" << endl;

    // print the clusters once the algorithm has converged
    for(int i=0; i<num_clusters; i++){
        clusters[i].print();
    }

    export_result();
    return 0;
}

// load dataset from file and store each point inside the array declared in the beginning
int load_dataset(bool iris_dataset){
    stringstream ss;
    if(iris_dataset){
        ss << base_dir << "input\\iris.txt";
    } else {
        ss << base_dir << "input\\" << num_points << "points-1.txt";
    }
    string filepath = ss.str();
    ifstream infile(filepath);
    if(!infile){
        cerr << "Could not open file. Maybe the number of points set is wrong?" << std::endl;
    }
    double x, y;
    int i=0;
    while(infile >> x >> y){
        Point point((double) x, (double) y);
        points[i] = point;
        i++;
    }
    return i;
}

// initialize random pivoting elements as many as the number of clusters
int init_clusters(){
    int i=0;
    for(i; i<num_clusters; i++){
        double x = rand() % 100 + 1;
        double y = rand() % 100 + 1;
        Cluster cluster = Cluster(Point((double) x, (double) y));
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
        int old_cluster_index = points[i].get_cluster();
        if (old_cluster_index == min_cluster_index){
            has_converged = true;
        } else {
            updates++;
            points[i].set_cluster(min_cluster_index);
        }
        // cout << "point set to cluster " << points[i].get_cluster() << endl;
        clusters[min_cluster_index].add_point(points[i]);
    }
    has_converged = (updates == 0);
    return has_converged;
}

// compute the distance between two 2D points (pythagorean theorem)
double distance(Point point, Cluster cluster){
    double d = sqrt(pow(point.get_x() - cluster.get_pivot().get_x(), 2) +
                    pow(point.get_y() - cluster.get_pivot().get_y(), 2));
    return d;
}

// export algorithm result to a file to process it using python (plotting, mostly)
void export_result(){
    stringstream ss;
    ss << base_dir << "output\\" << "res.txt";
    string filepath = ss.str();
    ofstream outfile(filepath);
    if(!outfile){
        cout << "file can't be opened" << endl;
    }
    for(int i=0; i<num_points; i++){
        outfile << points[i].get_x() << " " << points[i].get_y() << " " << points[i].get_cluster() << endl;
    }
    outfile.close();
}