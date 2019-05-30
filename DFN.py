import distributions as dist
import fracture as frac
import numpy as np
import plotly.graph_objs as go
import plotly.offline as poff
import dill
import matlab_clones as mc


class DiscreteFractureNetwork:
    """
    Classe per la descrizione del DiscreteFractureNetwork
    """

    def __init__(self, N, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax,
                 alpha_pl, radius_l, radius_u, k, mode_vector, fixed_n_edges=0):
        """
        Costruttore della classe
        :param N: numero di fratture
        :param Xmin, Xmax, Ymin, Ymax, Zmin, Zmax: estremi del dominio del DFN
        :param alpha_pl: parametro (> 1) della distribuzione Power LawBounded per i semiassi delle ascisse
        :param radius_l: limite inferiore dei semiassi delle ascisse
        :param radius_u: limite superiore dei semiassi delle ascisse
        :param k: parametro di concentrazione della legge Von Mises-Fisher
        :param mode_vector: punto medio della legge Von Mises-Fisher
        :param fixed_n_edges: numero fissato dei lati dei poligoni (> 2); se non specificato ogni poligono ha
        un numero casuale di lati da 8 a 16 (distribuiti uniformemente)
        """

        # N = numero delle fratture richieste
        self.N = 0  # il valore verrà poi aggiornato nel metodo genfrac

        # Definisco gli estremi del dominio del DFN
        # (ovvero la regione dello spazio in cui si trovano i baricentri delle fratture)
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax
        self.Zmin = Zmin
        self.Zmax = Zmax

        self.fixed_n_edges = fixed_n_edges

        # Definisco i parametri della distribuzione PowerLawBounded (pl_dist)
        self.alpha_pl = alpha_pl
        self.radius_l = radius_l
        self.radius_u = radius_u
        # Definisco la distribuzione power law bounded per i semiassi delle x
        self.pl_dist = dist.PowerLawBounded(alpha=alpha_pl, radius_l=radius_l, radius_u=radius_u)

        # Definisco i parametri della distribuzione Von Mises-Fisher (vmf_dist)
        # e normalizzo opportunamente mode_vector in caso non fosse di norma unitaria
        self.k = k
        self.mode_vector = mode_vector / np.linalg.norm(mode_vector)
        # qui sto definendo la distribuzione Von Mises-Fisher, k è il parametro di concentrazione
        # (parametro della distribuzione), mode_vector è un vettore di modulo unitario
        self.vmf_dist = dist.VonMisesFisher(k=k, mode_vector=self.mode_vector)

        # Creo la lista di poligoni che verra' aggiornata in genfrac
        self.fractures = []

        # Lista di liste con le possibili intersezioni, aggiornata in genfrac
        self.poss_intersezioni = []

        # Lista di liste con le effettive intersezioni
        self.intersezioni = []  # da non confondere il metodo con l'attributo (omonimi)

        # Lista di liste con le tracce per ogni poligono
        self.frac_traces = []

        # Lista con tutte le tracce del DFN
        self.traces = []

        self.genfrac(N)

    def genfrac(self, n_to_gen):
        """
        Genera n_to_gen fratture e le stampa
        :param n_to_gen: numero di fratture da generare
        """

        # Crea un vettore di n_togen semiassi (maggiori) dell'asse X nell'intervallo [radius_l,radius_u]
        semiaxes_x = self.pl_dist.sample(n_to_gen)

        # ars è aspect ratio, ovvero il rapporto tra semiasse delle X e semiasse delle Y, dato da un'uniforme definita in [1,3]
        ars = np.random.uniform(1, 3, n_to_gen)

        # normals mi dà una "matrice" 3xn_togen con le normali come vettori colonna
        normals = self.vmf_dist.sample(n_to_gen)

        # n_edges genera il numero di lati (un numero intero positivo) in maniera randomica tra 8 e 16
        # oppure li fissa a un valore se specificato nel costruttore

        if self.fixed_n_edges == 0:
            n_edges = np.random.random_integers(8, 16, n_to_gen)
        else:
            n_edges = [self.fixed_n_edges] * n_to_gen


        # alpha_angles sarebbe l'angolo di rotazione attorno alla normale (ovviamente sempre sul piano)
        alpha_angles = np.random.uniform(0, 2 * np.pi, n_to_gen)

        # generazione randomica dei baricentri dei poligoni, i quali sono inseriti in una matrice n_to_gen x 3
        centers = np.random.uniform(np.array([self.Xmin, self.Ymin, self.Zmin]),
                                    np.array([self.Xmax, self.Ymax, self.Zmax]),
                                    (n_to_gen, 3))

        # print("Qui di seguito sono i valori:\n\n","\n\nIl vettore dei semiassi:\n\n",semiaxes_x,"\n\nAspect Ratio:\n\n",ars,
        #      "\n\nVettore delle normali:\n\n",normals,"\n\nVettore del numero dei lati\n\n",n_edges,
        # "\n\nVettore degli angoli di rotazione attorno alla normale, sul piano:\n\n",alpha_angles,"\n\nVettore dei baricentri dei poligoni:\n\n",centers)

        # Creo i poligoni e li inserisco nella lista
        for i in range(n_to_gen):
            tmp = frac.Fracture(n_edges[i], semiaxes_x[i], alpha_angles[i], ars[i], normals[:, i], centers[i, :])
            self.fractures.append(tmp)

        # Aggiorno gli attributi: se sto creando una nuova istanza chiamo il metodo possibili_intersezioni,
        # altrimenti se sto aggiungendo poligoni ad una istanza già creata, aggiorno la lista di adiacenza
        # in modo più efficiente
        if self.N == 0:
            self.N += n_to_gen
            self.poss_intersezioni = self.possibili_intersezioni()
        else:
            for i in range(n_to_gen):
                self.poss_intersezioni.append([])
            for i in range(self.N):
                for j in range(n_to_gen):
                    if self.inters_BB(self.fractures[i], self.fractures[self.N + j]) is True:
                        self.poss_intersezioni[i].append(self.N + j)
                        self.poss_intersezioni[self.N + j].append(i)
            self.N += n_to_gen

    def rimuovi(self, v):
        """
        Rimuove le fratture nelle posizioni indicate dalla lista v (tenendo conto che l'indice parte da 0)
        Ad esempio se v = [2,4] il metodo rimuove il terzo poligono e il quinto
        :param v: lista contenente gli indici dei poligoni da rimuovere
        """

        # Ordino in senso decrescente il vettore v e elimino eventuali indici ripetuti
        # (un set in Python non ammette elementi uguali)
        # Non perdo in efficienza in quanto il metodo e' pensato per eliminare un numero molto piu' piccolo
        # del numero di fratture totali

        v = sorted(v, reverse=True)
        v = list(set(v))

        # Elimino le fratture richieste e aggiorno la lista di adiacenza poss_intersezioni
        for i in v:
            self.fractures.pop(i)
            self.poss_intersezioni.pop(i)
            for j in range(len(self.poss_intersezioni)):
                if i in self.poss_intersezioni[j]:
                    self.poss_intersezioni[j].remove(i)
                for k in range(len(self.poss_intersezioni[j])):
                    if self.poss_intersezioni[j][k] > i:  # rinumero
                        self.poss_intersezioni[j][k] -= 1

        # Aggiorno gli attributi
        self.N = self.N - len(v)

    def possibili_intersezioni(self):
        """
        Metodo che guarda ai Bounding Box delle fratture per una prima scrematura su possibili intersezioni.
        :return: lista di liste tale che l'i-esima lista contenga gli indici delle fratture del DFN con BB intersecante
        il BB dell'i-esimo poligono
        """
        # ovvero lista di adiacenza del grafo associato:
        # due poligoni sono collegati da un arco se i loro BB si intersecano

        # Creo una lista self.N liste vuote
        l = []
        for i in range(self.N):
            l.append([])

        for i in range(self.N - 1):
            for j in range(i + 1, self.N):
                if self.inters_BB(self.fractures[i], self.fractures[j]) is True:
                    l[i].append(j)
                    l[j].append(i)
        return l

    def inters_BB(self, fr1, fr2):
        """
        Metodo per controllare se i bounding box di due fratture si intersecano
        :param fr1: oggetto della classe Fracture
        :param fr2: oggetto della classe Fracture
        :return: booleano
        """

        max_x_min = max(fr1.xmin, fr2.xmin)
        min_x_max = min(fr1.xmax, fr2.xmax)
        max_y_min = max(fr1.ymin, fr2.ymin)
        min_y_max = min(fr1.ymax, fr2.ymax)
        max_z_min = max(fr1.zmin, fr2.zmin)
        min_z_max = min(fr1.zmax, fr2.zmax)
        if max_x_min <= min_x_max and max_y_min <= min_y_max and max_z_min <= min_z_max:
            return True
        else:
            return False


    def scrittura1(self):
        """
        Metodo per scrivere su file come richiesto al punto 7
        """

        with open('file1.txt', 'w') as f1:
            print(self.N, file=f1)
            for i in range(self.N):
                print(i, self.fractures[i].n, file=f1)
                for j in range(self.fractures[i].n):
                    print(self.fractures[i].vertici[0, j],
                          self.fractures[i].vertici[1, j],
                          self.fractures[i].vertici[2, j], file=f1)

    def scrittura2(self):
        """
        Metodo per scrivere su file come richiesto al punto 8
        """

        with open('file2.txt', 'w') as f2:
            print(self.N, file=f2)

            somma_vertici = 0
            for i in range(self.N):
                somma_vertici = somma_vertici + self.fractures[i].n
            print(somma_vertici, file=f2)

            indice = 0
            for i in range(self.N):
                print(i, self.fractures[i].n, indice, file=f2)
                indice = indice + self.fractures[i].n

            for i in range(self.N):
                for j in range(self.fractures[i].n):
                    print(self.fractures[i].vertici[0, j],
                          self.fractures[i].vertici[1, j],
                          self.fractures[i].vertici[2, j], file=f2)

    def visual3D(self):
        """
        Metodo per la visualizzazione grafica delle fratture
        """

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

            # Per controllare se un poligono e' parallelo a un piano coordinato che tolleranza devo usare???
            if np.linalg.norm(self.fractures[i].vn - np.array([1, 0, 0])) < 1.0e-15:
                area.delaunayaxis = 'x'
            elif np.linalg.norm(self.fractures[i].vn - np.array([0, 1, 0])) < 1.0e-15:
                area.delaunayaxis = 'y'
            elif np.linalg.norm(self.fractures[i].vn - np.array([0, 0, 1])) < 1.0e-15:
                area.delaunayaxis = 'z'

            all_polygons.append(perimetro)
            all_polygons.append(area)

        fig_3d_alltogether = go.Figure(data=all_polygons)
        poff.plot(fig_3d_alltogether)

    def save(self):
        """
        Salva l'oggetto DiscreteFractureNetwork come file .pkl
        """

        with open('DFN.pkl', 'wb') as f3:
            dill.dump(self, f3)

    def intersezioni(self):
        """
        Metodo per determinare le effettive intersezioni tra i poligoni
        :return: lista di liste tale che l'i-esima lista contenga gli indici delle fratture del DFN effettivamente
        intersecanti l'i-esimo poligono
        """

        # Creo una lista self.N liste vuote
        l = []
        for i in range(self.N):
            l.append([])


    def gen_trace(self, p1, p2):
        """
        Metodo per calcolare la traccia tra due poligoni
        :param p1: oggetto della classe Fracture
        :param p2: oggetto della classe Fracture
        :return: oggetto della classe Trace
        """

        # Calcoliamo la retta d'intersezione tra i poligoni
        # X(s) = r0 + s*t, dove s e' il parametro libero
        t = np.cross(p1.vn, p2.vn)  # direzione della retta
        A = np.array([p1.vn, p2.vn, t])
        b = np.zeros(3)
        b[0] = np.dot(p1.vertici[:, 0], p1.vn)
        b[1] = np.dot(p2.vertici[:, 0], p2.vn)
        b[2] = 0
        r0 = np.linalg.solve(A, b)  # un generico punto della retta

        # Ruotiamo il poligono p1 per ricondurci sul piano
        # Sul file c'è scritto di ruotare e poi traslare, mentre noi abbiamo prima traslato e poi ruotato,
        # in modo da avere la configurazione iniziale sul piano xy
        # A causa di approssimazioni non otteniamo esattamente 0 come coordinate z, ma numeri dell'ordine di grandezza
        # di 1.0e-16

        # STIAMO SCRIVENDO 2 VOLTE DEL CODICE UGUALE,
        # PUO' AVERE SENSO ITERARE 2 VOLTE CON UN FOR O USARE UN'ALTRA FUNZIONE

        # QUANDO CAPISCO CHE POSSO NON AVERE INTERSEZIONE???

        rotMatrix_1 = np.dot(np.dot(mc.rotz(- p1.alpha), mc.roty(p1.phi - np.pi / 2)), mc.rotz(- p1.teta))
        vertici_1 = p1.vertici
        for i in range(p1.n):
            vertici_1[:, i] -= p1.bar
        vertici_1 = np.dot(rotMatrix_1, vertici_1)
        t_1 = np.dot(rotMatrix_1, t)
        r0_1 = np.dot(rotMatrix_1, r0 - p1.bar)

        rotMatrix_2 = np.dot(np.dot(mc.rotz(- p2.alpha), mc.roty(p2.phi - np.pi / 2)), mc.rotz(- p2.teta))
        vertici_2 = p2.vertici
        for i in range(p2.n):
            vertici_2[:, i] -= p2.bar
        vertici_2 = np.dot(rotMatrix_2, vertici_2)
        t_2 = np.dot(rotMatrix_2, t)
        r0_2 = np.dot(rotMatrix_2, r0 - p2.bar)

        # Stampo per verifica (da togliere)
        print(vertici_1)
        print(r0_1)
        print(vertici_2)
        print(r0_2)

        # Effettuate le rotazioni, per ogni poligono dobbiamo trovare la traccia effettiva e salvarla


r = DiscreteFractureNetwork(5, 3, 10, -2, 8, 2, 9, 2, 4, 4, 0.1, np.array([[0.5], [2.], [1.]]), 8)
# r.scrittura1()
# r.visual3D()
# r.scrittura2()
print(r.poss_intersezioni)
r.rimuovi([0, 0, 1])
# print("Indici aggiornati")
print(r.poss_intersezioni)
r.genfrac(2)
print(r.poss_intersezioni)

# r.gen_trace(r.fractures[0], r.fractures[1])

# Codice per testare salvataggio su file .pkl
# r.save()
# with open('DFN.pkl', 'rb') as f4:
#     r1 = dill.load(f4)
# r1.visual3D()


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
