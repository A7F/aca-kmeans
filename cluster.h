#ifndef CLUSTER_H
#define CLUSTER_H

#include "point.h"

class Cluster{
public:
    Cluster(){
        this->pivot = Point();
        this->new_pivot = Point();
        this->dimension = 0;
    }
    Cluster(Point pivot){
        this->pivot = pivot;
        this->new_pivot = Point();
        this->dimension = 0;
    }

    // set cluster pivoting point
    void set_pivot(Point point){
        this->pivot = point;
    }

    // get cluster pivoting point
    Point get_pivot(){
        return this->pivot;
    }

    // set new pivot coordinates
    void set_new_pivot(Point point){
        this->new_pivot = point;
    }

    // get new coordinates for new pivot
    Point get_new_pivot(){
        return this->new_pivot;
    }

    // get the total number of points belonging to the cluster
    int get_dimension(){
        return this->dimension;
    }

    // set total number of points belonging to the cluster. This method should reset the variable at each iteration
    void set_dimension(int dimension){
        this->dimension=dimension;
    }

    void add_point(Point point){
        this->new_pivot.set_x(new_pivot.get_x() + point.get_x());
        this->new_pivot.set_y(new_pivot.get_y() + point.get_y());
        dimension++;
    }

    void empty_pivot(){
        this->dimension = 0;
        this->new_pivot.set_x(0);
        this->new_pivot.set_y(0);
    }

    // update centroid by setting the new coordinates as current
    void update_centroid(){
        this->pivot.set_x(this->new_pivot.get_x() / this->dimension);
        this->pivot.set_y(this->new_pivot.get_y() / this->dimension);
    }

    void print(){
        std::cout << "cluster has dimension " << dimension << " and pivot (" << this->pivot.get_x() << ", " << this->pivot.get_y() << ")" << std::endl;
    }

private:
    Point pivot;
    Point new_pivot;
    int dimension;
};

#endif //CLUSTER_H
