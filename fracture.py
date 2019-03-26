import numpy as np
import scipy as sp
from Progetto import matlab_clones as mc

class Fracture():
    '''
    Classe per la descrizione delle fratture
    '''

    def __init__(self, n, rx, alpha, ar, v, bar ):

        #NON HO ANCORA TESTATO SE IL COSTRUTTORE FUNZIONA E SE NON CI SONO ERRORI

        #N.B i vettori v e bar sono vettori colonna

        #alpha, teta e phi sono usati analogamente al pdf della descrizione del progetto

        self.n = n
        self.rx = rx
        self.ry = rx / ar
        self.alpha = alpha
        self.teta = mc.cart2sph(v[0], v[1], v[2])[0]
        self.phi = mc.cart2sph(v[0], v[1], v[2])[1]
        self.vn = v
        self.vertici = np.zeros((3, n))     #prealloco la matrice dei vertici perché ne conosco le dimensioni

        # ciclo for per generare i vertici del poligono
        for i in range(n):
            self.vertici[0, i] = self.rx * np.cos(i * 2 * np.pi / n)
            self.vertici[1, i] = self.ry * np.sin(i * 2 * np.pi / n)

        #Genero la matrice di rotazione, ruoto i vertici
        rotMatrix = np.dot(np.dot(mc.rotz(self.teta), mc.roty(np.pi / 2 - self.phi)), mc.rotz(alpha))
        self.vertici = np.dot(rotMatrix, self.vertici)

        #Traslo i vertici
        for i in range(n):
            self.vertici[:, i] = self.vertici[:, i] + bar

        #Trovo il Bounding box

        self.xmin = np.min(self.vertici[0, :])
        self.xmax = np.max(self.vertici[0, :])
        self.ymin = np.min(self.vertici[1, :])
        self.ymax = np.max(self.vertici[1, :])
        self.zmin = np.min(self.vertici[2, :])
        self.zmax = np.max(self.vertici[2, :])








