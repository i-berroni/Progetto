#include <iostream>
#include <string>
#include <math.h>
using namespace std;

class Point2D{
        private: 
            float x, y;
            
        public:
        
        Point2D(float i);
        Point2D(float i , float j);
        ~Point2D(); 
        Point2D(const Point2D &);
    Point2D operator+(Point2D &);
    Point2D operator-(Point2D &);
    void show();
    float getx();
    float gety();
    float norm();
};