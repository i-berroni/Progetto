#include <iostream>
#include <string>
#include <math.h>
#include "Point2D.hpp"
using namespace std;

void Point2D::show(){cout<<"("<<x<<","<<y<<")";};
float Point2D::getx(){
            return x;
        }
float Point2D::gety(){
            return y;
        }
float Point2D::norm(){        
            return sqrt(x*x+y*y);
    }
Point2D::Point2D(float i)         // il costruttore deve avere lo stesso nome della classe
        {
            
                    x=i;
                    y=i;
        }    
Point2D::Point2D(float i, float j)// il costruttore deve avere lo stesso nome della classe
        {
            
                    x=i;
                    y=j;
        } 
Point2D::~Point2D()// il distruttore non vuole parametri
        {
            cout <<"\nDestructor called\n";
        } 
Point2D::Point2D(const Point2D &point){
x=point.x;
y=point.y;

}
//Operatore di somma
Point2D Point2D::operator+ (Point2D &a)
{
        return Point2D(x+a.x,y+a.y);
}
//Operatore di differenza
Point2D Point2D::operator- (Point2D &a)
{
        return Point2D(x-a.x,y-a.y);
}

main(){
float norma, a, b, c, d; 
Point2D somm;
Point2D diff;
cout <<"Immetti i valori dell'oggetto 1 che vuoi creare e premi invio\n";
cout <<"primo elemento:\n";
cin >> a;
cout <<"secondo elemento:\n";
cin >> b;
Point2D m(a,b);
cout <<"Immetti i valori dell'oggetto 2 che vuoi creare e premi invio\n";
cout <<"primo elemento:\n";
cin >> c;
cout <<"secondo elemento:\n";
cin >> d;
Point2D f(c,d);
cout <<"\nQuesto e' l'oggetto creato con il costruttore:\n";
m.show();
Point2D n=m; //serve a copiare il contenuto dell'oggetto m in un nuovo oggetto n con gli stessi attributi
cout <<"\nQuesto e' l'oggetto copiato con il costruttore di copia:\n";
n.show();
cout <<"\nQuesta e' la norma:\n";
norma=n.norm();
cout << norma;
cout <<"\nQuesta e' la somma:\n";
somm=m+f;
diff=m-f;




return 0;


};




















