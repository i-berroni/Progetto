#include <iostream>
#include <string>
#include <math.h>
#include "Edge.hpp"
using namespace std;
//costruttori
Edge::Edge(){


        }
Edge::Edge(Point2D point1,Point2D point2)
        {
                p1=point1;
                p2=point2;
        }

//distruttore
Edge::~Edge()
        {
            cout <<"\nDestructor called\n";
        }
//costruttore di copia
Edge::Edge(const Edge &edge){
p1=edge.p1;
p2=edge.p2;
}
//metodi di accesso
Point2D Edge::getp1(){
        return p1;
        }
Point2D Edge::getp2(){
        return p2;
        }
float Edge::getx1(){
            return p1.getx();
        }
float Edge::gety1(){
            return p1.gety();
        }
float Edge::getx2(){
            return p2.getx();
        }
float Edge::gety2(){
            return p2.gety();
        }
//Lunghezza del lato
float Edge::length(){

            return sqrt((getx2()-getx1())*(getx2()-getx1())+((gety2()-gety1())*(gety2()-gety1())));
    }


