from Progetto import distributions as dist
from Progetto import fracture as frac
import numpy as np

class DiscreteFractureNetwork:

    def __init__(self, N, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax, alpha_pl, radius_l, radius_u, k, mode_vector):

        # N = numero delle fratture richieste
        self.N = N

        # Definisco gli estremi del dominio del DFN
        # (ovvero la regione dello spazio in cui si trovano i baricentri delle fratture)
        # il nome delle variabili e' uguale a quelle del Bounding Box della classe Fracture, e' un problema???
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax
        self.Zmin = Zmin
        self.Zmax = Zmax

        # Definisco i parametri della distribuzione PowerLawBounded (pl_dist)
        self.alpha_pl = alpha_pl
        self.radius_l = radius_l
        self.radius_u = radius_u
        # qui sto definendo la distribuzione power law bounded per i semiassi delle x
        self.pl_dist = dist.PowerLawBounded(alpha=alpha_pl, radius_l=radius_l, radius_u=radius_u)

        # Definisco i parametri della distribuzione Von Mises-Fisher (vmf_dist)
        # e normalizzo opportunamente mode_vector in caso non fosse di norma unitaria
        self.k = k
        self.mode_vector = mode_vector / np.linalg.norm(mode_vector)
        # qui sto definendo la distribuzione Von Mises-Fisher, k è il parametro di concentrazione
        # (parametro della distribuzione), mode_vector è un vettore di modulo unitario
        self.vmf_dist = dist.VonMisesFisher(k=k, mode_vector=mode_vector)

        # questo è un vettore di poligoni che si rifà alla classe fracture(che, appunto, è una classe che rappresenta il poligono)
        # DA FARE
        # Come struttura dati è meglio usare una lista in quanto sequenza mutabile di oggetti;
        # possiamo usare i metodi append, insert, pop, remove per gestirla e inserire e/o rimuovere fratture come richiesto dal progetto
        self.fractures = []
        self.genfrac(self.N)


    def genfrac(self, n_togen):

        '''
        Genera n_togen fratture e le stampa
        '''

        # semiaxes_x mi restituisce un vettore di n_togen semiassi (maggiori) dell'asse X nell'intervallo [radius_l,radius_u]
        semiaxes_x = self.pl_dist.sample(n_togen)

        # ars è aspect ratio, ovvero il rapporto tra semiasse delle X e semiasse delle Y, dato da un'uniforme definita in [1,3]
        ars = np.random.uniform(1, 3, n_togen)

        # normals mi dà una "matrice" 3xn_togen con le normali come vettori colonna
        normals = self.vmf_dist.sample(n_togen)

        # n_edges genera il numero di lati (un numero intero positivo) in maniera randomica tra 8 e 16
        n_edges = np.random.random_integers(8, 16, n_togen)

        # alpha_angles sarebbe l'angolo di rotazione attorno alla normale (ovviamente sempre sul piano)
        alpha_angles = np.random.uniform(0, 2 * np.pi, n_togen)

        # generazione randomica dei baricentri dei poligoni, i quali sono inseriti in una matrice n_togenx3
        centers = np.random.uniform(np.array([self.Xmin, self.Ymin, self.Zmin]),
                                    np.array([self.Xmax, self.Ymax, self.Zmax]),
                                    (n_togen, 3))

        print("Qui di seguito sono i valori:\n\n","\n\nIl vettore dei semiassi:\n\n",semiaxes_x,"\n\nAspect Ratio:\n\n",ars,
              "\n\nVettore delle normali:\n\n",normals,"\n\nVettore del numero dei lati\n\n",n_edges,
        "\n\nVettore degli angoli di rotazione attorno alla normale, sul piano:\n\n",alpha_angles,"\n\nVettore dei baricentri dei poligoni:\n\n",centers)

        # Creo i poligoni e li inserisco nella lista
        for i in range(n_togen):
            tmp = frac.Fracture(n_edges[i], semiaxes_x[i], alpha_angles[i], ars[i], normals[:,i], centers[i,:])
            self.fractures.append(tmp)

    def rimuovi(self, v):
        '''
        Rimuove le fratture nelle posizioni indicate dal vettore v (tenendo conto che l'indice parte da 0)
        Ad esempio se v = [2,4] il metodo rimuove il terzo poligono e il quinto
        '''
        #print(len(v))
        #print("questo è range",range(len(v)))
        for i in range(len(v)):
            self.fractures.pop(v[#???])
            # DA CAPIRE QUALE INDICE METTERE




# Creo un oggetto dove inizializzo variabili che decido io
# e poi modifico il metodo di genfrac
# per fargli stampare i dati dell'asse x
r = DiscreteFractureNetwork(3, 0, 1, 0, 1, 0, 1, 2, 3, 4, 2, np.array([[0.], [0.], [1.]]))
print(r.fractures)
r.genfrac(2)
print(r.fractures)
r.rimuovi([2,3,4])
print(r.fractures)

