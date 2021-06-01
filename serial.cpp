#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ctime>
#include <cmath>
#include <chrono>
#include "point.h"
#include "cluster.h"

using namespace std;

// define how many clusters of points we want and the total number of points
const int num_clusters = 10;
const int num_points = 300000;
const int max_iters = 100;

// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";

/**
* specify here which dataset you want to use. Datasets available:
* "points" = random points
* "iris" = iris dataset, 3 clusters known, 150 points
* "blobs" = synthetic clusters generated from sk-learn with function make_blobs. Set cluster and points accordingly
**/
const string dataset = "points";


// defining data and functions
int load_dataset(string dataset);
int init_clusters();
double distance(Point point, Cluster cluster);
int random(int min, int max);
void naive_kmeans();
void export_result(int iterations, double serial_time, double convergence_time);
Point points[num_points];
Cluster clusters[num_clusters];


int main(){
    srand(time(NULL));
    // load the dataset. Use flag true if you want to test with iris dataset
    double time_point1 = omp_get_wtime();
    int tot_points = load_dataset(dataset);
    cout << "total points loaded: " << tot_points << endl;
    int tot_clusters = init_clusters();
    cout << "total clusters instantiated: " << tot_clusters << endl;
    for(int i=0; i<num_clusters; i++){
        clusters[i].print();
    }
    double time_point2 = omp_get_wtime();
    double duration = time_point2 - time_point1;
    bool converged = false;

    // algorithm start. Compute distances between each point and centroids
    int iteration = 0;
    while(!converged && iteration < max_iters){
        iteration++;
        // double stop1 = omp_get_wtime();
        naive_kmeans();
        // double stop2 = omp_get_wtime();
        // reset dimension for all the clusters before starting a new iteration
        for(int i=0; i<num_clusters; i++){
            converged = clusters[i].update_centroid();
            clusters[i].empty_pivot();
        }
        // double stop3 = omp_get_wtime();
        // printf("kmeans took %f s\tupdate centroids took %f s\n", stop2-stop1, stop3-stop2);
        printf(">>> Iteration %d done <<<\n", iteration);
    }

    cout << endl << "======= results after convergence (" << iteration << " iters) =======" << endl;

    // print the clusters once the algorithm has converged
    for(int i=0; i<num_clusters; i++){
        clusters[i].print();
    }
    double time_point3 = omp_get_wtime();
    double serial_time = duration;
    duration = time_point3 - time_point2;

    printf("Number of iterations: %d, total time: %f seconds, time per iteration: %f seconds\n",
           iteration, duration, duration/iteration);

    export_result(iteration, serial_time, duration);
    return 0;
}

// load dataset from file and store each point inside the array declared in the beginning.
// datasets available are "iris", "points" or "blobs".
int load_dataset(string dataset){
    stringstream ss;
    if(dataset=="iris"){
        ss << base_dir << "input\\iris.txt";
    }
    if(dataset=="points"){
        ss << base_dir << "input\\" << num_points << "points.txt";
    }
    if(dataset=="blobs"){
        ss << base_dir << "input\\" << num_points << "-" << num_clusters << "-blob.txt";
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
    int index=0;
    for(index; index<num_clusters; index++){
        int random_point_index = random(0, num_points);
        double x = points[random_point_index].get_x();
        double y = points[random_point_index].get_y();
        Cluster cluster = Cluster(Point((double) x, (double) y, index));
        clusters[index] = cluster;
    }
    return index;
}

//compute the distance between all the points and centroids
void naive_kmeans(){
    double min_distance;
    int min_cluster_index;

    for(int i=0; i<num_points; i++){
        min_distance = distance(points[i], clusters[0]);
        min_cluster_index = 0;
        for(int j=0; j<num_clusters; j++){
            double tmp_distance = distance(points[i], clusters[j]);
            // printf("distance with cluster %i pivot (%f, %f): %f\n", j, clusters[j].get_pivot().get_x(), clusters[j].get_pivot().get_y(), tmp_distance);
            if(tmp_distance<min_distance){
                min_distance = tmp_distance;
                min_cluster_index = j;
            }
        }
        points[i].set_cluster(min_cluster_index);
        clusters[min_cluster_index].add_point(points[i]);
    }
}

// compute the distance between two 2D points (pythagorean theorem)
double distance(Point point, Cluster cluster){
    double d = sqrt(pow(point.get_x() - cluster.get_pivot().get_x(), 2) + pow(point.get_y() - cluster.get_pivot().get_y(), 2));
    return d;
}

int random(int min, int max){
    return min + rand() % (( max + 1 ) - min);
}

// export algorithm result to a file to process it using python (plotting, mostly)
void export_result(int iterations, double serial_time, double convergence_time){
    stringstream ss;
    ss << base_dir << "output\\" << "res.txt";
    string filepath = ss.str();
    ofstream outfile(filepath);
    if(!outfile){
        cout << "file res can't be opened" << endl;
    }
    outfile << num_clusters << endl;
    for(int i=0; i<num_clusters; i++){
        outfile << clusters[i].get_pivot().get_x() << " " << clusters[i].get_pivot().get_y() << " " << clusters[i].get_pivot().get_cluster() << endl;
    }
    for(int i=0; i<num_points; i++){
        outfile << points[i].get_x() << " " << points[i].get_y() << " " << points[i].get_cluster() << endl;
    }
    outfile.close();

    ofstream statfile;
    string dir = base_dir + "output\\runs.csv";
    statfile.open(dir, ios_base::app);
    if(!statfile){
        cout << "file runs can't be opened" << endl;
    }
    const auto p1 = std::chrono::system_clock::now();
    long timestamp = std::chrono::duration_cast<std::chrono::seconds>(p1.time_since_epoch()).count();
    int threads = 1;
    statfile <<timestamp<<","<<"s,c,"<<dataset<<","<<num_points<<","<<num_clusters<<","<<threads<<","<<iterations<<","<<serial_time<<","<<convergence_time<<endl;
}