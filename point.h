#ifndef POINT_H
#define POINT_H


class Point {
public:
    Point(){
        this->x = 0;
        this->y = 0;
        this->cluster = 0;
    }
    Point(double x_coord, double y_coord){
        this->x = x_coord;
        this->y = y_coord;
        this->cluster = 0;
    }
    Point(double x_coord, double y_coord, int cluster_number){
        this->x = x_coord;
        this->y = y_coord;
        this->cluster = cluster_number;
    }
    // set x coordinate
    void set_x(double x_coord){
        this->x = x_coord;
    }
    // get x coordinate
    double get_x(){
        return this->x;
    }
    // set y coordinate
    void set_y(double y_coord){
        this->y = y_coord;
    }
    // get y coordinate
    double get_y(){
        return this->y;
    }
    // set cluster to which the point belongs to
    void set_cluster(int cluster_id){
        this->cluster = cluster_id;
    }
    // get cluster id to which the point belongs to
    int get_cluster(){
        return this->cluster;
    }

private:
    double x;
    double y;
    int cluster;
};


#endif //POINT_H
