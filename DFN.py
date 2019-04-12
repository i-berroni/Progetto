import distributions as dist
import fracture as frac
import numpy as np
import plotly.graph_objs as go
import plotly.offline as poff


class DiscreteFractureNetwork:

    def __init__(self, N, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax, alpha_pl, radius_l, radius_u, k, mode_vector):

        # N = numero delle fratture richieste
        self.N = 0  # il valore verrà poi aggiornato nel metodo genfrac

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
        self.vmf_dist = dist.VonMisesFisher(k=k, mode_vector=self.mode_vector)

        # questo è una lista di poligoni che si rifà alla classe fracture(che, appunto, è una classe che rappresenta il poligono)
        # e viene aggiornata nel metodo genfrac
        self.fractures = []

        # Lista di lista con le possibili intersezioni, aggiornata in genfrac
        self.poss_intersezioni = []

        self.genfrac(N)


    def genfrac(self, n_to_gen):

        '''
        Genera n_to_gen fratture e le stampa
        '''

        # semiaxes_x mi restituisce un vettore di n_togen semiassi (maggiori) dell'asse X nell'intervallo [radius_l,radius_u]
        semiaxes_x = self.pl_dist.sample(n_to_gen)

        # ars è aspect ratio, ovvero il rapporto tra semiasse delle X e semiasse delle Y, dato da un'uniforme definita in [1,3]
        ars = np.random.uniform(1, 3, n_to_gen)

        # normals mi dà una "matrice" 3xn_togen con le normali come vettori colonna
        normals = self.vmf_dist.sample(n_to_gen)

        # n_edges genera il numero di lati (un numero intero positivo) in maniera randomica tra 8 e 16
        n_edges = np.random.random_integers(8, 16, n_to_gen)

        # alpha_angles sarebbe l'angolo di rotazione attorno alla normale (ovviamente sempre sul piano)
        alpha_angles = np.random.uniform(0, 2 * np.pi, n_to_gen)

        # generazione randomica dei baricentri dei poligoni, i quali sono inseriti in una matrice n_togenx3
        centers = np.random.uniform(np.array([self.Xmin, self.Ymin, self.Zmin]),
                                    np.array([self.Xmax, self.Ymax, self.Zmax]),
                                    (n_to_gen, 3))

        print("Qui di seguito sono i valori:\n\n","\n\nIl vettore dei semiassi:\n\n",semiaxes_x,"\n\nAspect Ratio:\n\n",ars,
              "\n\nVettore delle normali:\n\n",normals,"\n\nVettore del numero dei lati\n\n",n_edges,
        "\n\nVettore degli angoli di rotazione attorno alla normale, sul piano:\n\n",alpha_angles,"\n\nVettore dei baricentri dei poligoni:\n\n",centers)

        # Creo i poligoni e li inserisco nella lista
        for i in range(n_to_gen):
            tmp = frac.Fracture(n_edges[i], semiaxes_x[i], alpha_angles[i], ars[i], normals[:,i], centers[i,:])
            self.fractures.append(tmp)

        # Aggiorno gli attributi
        self.N = self.N + n_to_gen
        self.poss_intersezioni = self.possibili_intersezioni()


    def rimuovi(self, v):
        '''
        Rimuove le fratture nelle posizioni indicate dal vettore v (tenendo conto che l'indice parte da 0)
        Ad esempio se v = [2,4] il metodo rimuove il terzo poligono e il quinto
        '''

        v = np.sort(v)      # ordino il vettore così da poter usare il metodo senza problemi
        for i in range(len(v)):
            self.fractures.pop(v[- i - 1])

        # Aggiorno gli attributi
        self.N = self.N - len(v)
        self.poss_intersezioni = self.possibili_intersezioni()


    def possibili_intersezioni(self):
        '''
        Metodo che guarda ai Bounding Box delle fratture per una prima scrematura su possibili intersezioni.
        Ritorna una lista di liste come richiesto al punto 9
        '''

        l = []

        # Questo primo for serve per riempire la lista L con self.N liste vuote
        for i in range(self.N):
            l.append([])
          #  l = [[]] * 5
        for i in range(self.N - 1):
            for j in range(i + 1, self.N):
                max_x_min = max(self.fractures[i].xmin, self.fractures[j].xmin)
                min_x_max = min(self.fractures[i].xmax, self.fractures[j].xmax)
                max_y_min = max(self.fractures[i].ymin, self.fractures[j].ymin)
                min_y_max = min(self.fractures[i].ymax, self.fractures[j].ymax)
                max_z_min = max(self.fractures[i].zmin, self.fractures[j].zmin)
                min_z_max = min(self.fractures[i].zmax, self.fractures[j].zmax)
                if max_x_min > min_x_max:
                    break
                elif max_y_min > min_y_max:
                    break
                elif max_z_min > min_z_max:
                    break
                else:
                    l[i].append(j)
                    l[j].append(i)
        return l


    def scrittura1(self):   # il metodo funziona e scrive su file, e' da migliorare la formattazione
        '''
        Metodo per scrivere su file come richiesto al punto 7
        '''

        with open('file1.txt', 'w') as f1:
            print(self.N, file=f1)
            for i in range(self.N):
                print(i, self.fractures[i].n, file=f1)
                for j in range(self.fractures[i].n):
                    print(self.fractures[i].vertici[0, j],
                          self.fractures[i].vertici[1, j],
                          self.fractures[i].vertici[2, j], file=f1)

    def visual3D(self):

        all_polygons = []
        for i in range(self.N):
            x = self.fractures[i].vertici[0, :].tolist()
            y = self.fractures[i].vertici[1, :].tolist()
            z = self.fractures[i].vertici[2, :].tolist()

            x.append(x[0])
            y.append(y[0])
            z.append(z[0])
            perimetro = go.Scatter3d(x=x, y=y, z=z,
                                 mode='lines',
                                 marker=dict(
                                     color='red'
                                 )
                                 )
            area = go.Mesh3d(x=x, y=y, z=z, color='#FFB6C1', opacity=0.60)

            all_polygons.append(perimetro)
            all_polygons.append(area)
            
        fig_3d_alltogether = go.Figure(data=all_polygons)
        poff.plot(fig_3d_alltogether)


    def scrittura2(self):
        '''
        Metodo per scrivere su file come richiesto al punto 8
        :return:
        '''




r = DiscreteFractureNetwork(10, 0, 5, 0, 5, 0, 5, 2, 2, 3, 2, np.array([[0.], [0.], [1.]]))
#r.scrittura1()
r.visual3D()



'''
# Creo un oggetto dove inizializzo variabili che decido io
# e poi modifico il metodo di genfrac
# per fargli stampare i dati dell'asse x
r = DiscreteFractureNetwork(3, 0, 5, 0, 5, 0, 5, 2, 2, 3, 2, np.array([[0.], [0.], [1.]]))
print(r.fractures)
print(r.N)
print(r.poss_intersezioni)
r.genfrac(2)
print(r.fractures)
print(r.N)
print(r.poss_intersezioni)
r.rimuovi([2,4,0])
print(r.poss_intersezioni)
# l = r.possibili_intersezioni()
# r.poss.intersezioni
# print(l)
'''
