#ifndef CLUSTER_H
#define CLUSTER_H

class Cluster{
public:
    Cluster(){
        this->pivot = Point();
        this->dimension = 0;
    }
    Cluster(Point pivot){
        this->pivot = pivot;
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

    // get the total number of points belonging to the cluster
    int get_dimension(){
        return this->dimension;
    }

    /**
    TODO:
    check if new coordinates are different than the current ones, if yes update centroid, otherwise centroid
    didn't move so this means that the algorithm converged for this specific cluster
    **/
    void update_centroid(Point point){
        this->dimension++;
        double old_x = this->pivot.get_x();
        double new_x = old_x + point.get_x() / this->dimension;
        this->pivot.set_x(new_x);
        double old_y = this->pivot.get_y();
        double new_y = old_y + point.get_y() / this->dimension;
        this->pivot.set_y(new_y);
    }

    void print(){
        std::cout << "cluster has dimension " << dimension << " and pivot (" << this->pivot.get_x() << ", " << this->pivot.get_y() << ")" << std::endl;
    }

private:
    Point pivot;
    int dimension;
};

#endif //CLUSTER_H
