import  distributions as dist
#import fracture as frac
import numpy as np



class DiscreteFractureNetwork:
    #metto in ordine: Estremi,punto 1, punto 2
    def __init__(self,N,xmin,xmax,ymin,ymax,zmin,zmax,alpha_pl,radius_l,radius_u, k, mode_vector):
        #N=numero delle fratture richieste
        self.N = N
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.alpha_pl = alpha_pl
        self.radius_l = radius_l
        self.radius_u = radius_u
        #qui sto definendo la distribuzione power law bounded per i semiassi delle x
        self.pl_dist = dist.PowerLawBounded(alpha=alpha_pl, radius_l=radius_l, radius_u=radius_u)
        #qui sto definendo la distribuzione Von Mises-Fischer, k è il parametro di concentrazione(parametro della distribuzione), mode_vector è un vettore di modulo unitario
        self.vmf_dist = dist.VonMisesFisher(k=k, mode_vector=mode_vector)

        # questo è un vettore di poligoni che si rifà alla classe fracture(che, appunto, è una classe che rappresenta il poligono)

        #genera la frattura e la stampa
    def genfrac(self):

        #semiaxes_x mi restituisce un vettore di N semiassi (maggiori) dell'asse X nell'intervallo [radius_l,radius_u]
        semiaxes_x = self.pl_dist.sample(self.N)

        #ars è aspect ratio, ovvero il rapporto tra semiasse delle X e semiasse delle Y, dato da un'uniforme definita in [1,3]
        ars = np.random.uniform(1, 3, self.N)

        #normals mi dà una "matrice" 3xN con le normali come vettori colonna
        normals = self.vmf_dist.sample(self.N)

        #n_edges genera il numero di lati (un numero intero positivo) in maniera randomica tra 8 e 16
        n_edges = np.random.random_integers(8, 16, self.N)

        #alpha_angles sarebbe l'angolo di rotazione attorno alla normale (ovviamente sempre sul piano)
        alpha_angles = np.random.uniform(0, 2 * np.pi, self.N)

        #generazione randomica dei baricentri dei poligoni, i quali sono inseriti in una matrice Nx3
        centers = np.random.uniform(np.array([self.xmin, self.ymin, self.zmin]),
                                    np.array([self.xmax, self.ymax, self.zmax]),
                                    (self.N, 3))

        print("Qui di seguito sono i valori:\n\n","\n\nIl vettore dei semiassi:\n\n",semiaxes_x,"\n\nAspect Ratio:\n\n",ars,
              "\n\nVettore delle normali:\n\n",normals,"\n\nVettore del numero dei lati\n\n",n_edges,
        "\n\nVettore degli angoli di rotazione attorno alla normale, sul piano:\n\n",alpha_angles,"\n\nVettore dei baricentri dei poligoni:\n\n",centers)


#Creo un oggetto dove inizializzo variabili che decido io
#e poi modifico il metodo di genfrac
#per fargli stampare i dati dell'asse x
r=DiscreteFractureNetwork(10,0,1,0,1,0,1,2,3,4,2,np.array([[0.],[0.],[1.]]))
r.genfrac()






