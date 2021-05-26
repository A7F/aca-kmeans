#ifndef CLUSTER_H
#define CLUSTER_H

class Cluster{
public:
    Cluster(){
        this->point = Point();
        this->dimension = 0;
    }
private:
    Point point;
    int dimension;
};

#endif //CLUSTER_H
