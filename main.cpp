#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

// define how many clusters of points we want and the total number of points
const int clusters = 3;
const int num_points = 50;
// specify here your absolute path to project folder
const string base_dir = R"(C:\Users\rockt\CLionProjects\aca-kmeans\)";

class Point{
public:
    int x;
    int y;
};

Point points[num_points];

void load_dataset(){
    std::stringstream ss;
    ss << base_dir << "input\\" << num_points << "points-1.txt";
    string filepath = ss.str();
    ifstream infile(filepath);
    if(!infile){
        cerr << "Could not open file" << std::endl;
    }
    int x, y, i=0;
    while(infile >> x >> y){
        Point point;
        point.x = x;
        point.y = y;
        points[i] = point;
        i++;
    }
}

int main(){
    load_dataset();
    return 0;
}