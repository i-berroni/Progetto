#include <iostream>
#include <string>
#include <math.h>
#include "Edge.hpp"
using namespace std;


main(){
//Here I declare the variables
float norma, a, b, c, d;
Point2D somm;
Point2D diff;
Edge lato;

//Here I do the inputs:
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

//Here I show the objects:
cout <<"\nQuesti sono gli oggetti con il costruttore:\n";
m.show();
f.show();
Point2D n=m; //serve a copiare il contenuto dell'oggetto m in un nuovo oggetto n con gli stessi attributi
cout <<"\nQuesto e' l'oggetto copiato con il costruttore di copia:\n";
n.show();

//Here I evaluate the norms:
cout <<"\nQuesta e' la norma del primo oggetto:\n";
norma=n.norm();
cout <<norma;

cout <<"\nQuesta e' la norma del secondo oggetto:\n";
norma=f.norm();
cout <<norma;


cout <<"\nQuesta e' la somma:\n";
somm=m+f;
diff=m-f;
somm.show();
diff.show();



//Here we go for the Edges:
cout<<"\nQui costruisco un Edge:\n";
lato=Edge(m,f);
lato.show();
//Here I show the length
cout<<lato.length();






return 0;


};

