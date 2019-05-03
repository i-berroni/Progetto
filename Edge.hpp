#include <iostream>
#include <string>
#include <math.h>
using namespace std;
#include "Point2D.hpp"

class Edge{
        private:
            Point2D p1,p2;

        public:
        //Prototipi dei costruttori:
        Edge();
        Edge(Point2D, Point2D);

        //Prototipo del distruttore
        ~Edge();

        //Prototipo del costruttore di copia
        Edge(const Edge &);

        void show(){
            cout<<"\nQuesto e' il lato richiesto.\n";
            cout<<"Punto iniziale: ("<<p1.getx()<<","<<p1.gety()<<")\n";
            cout<<"Punto finale: ("<<p2.getx()<<","<<p2.gety()<<")\n";
            };

    //Metodi di accesso alle coordinate
    Point2D getp1();
    Point2D getp2();
    float getx1();
    float gety1();
    float getx2();
    float gety2();
    //Lunghezza del lato
    float length();
};
