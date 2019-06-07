import DFN
import numpy as np
import matlab_clones as mc

# che import devo fare esattamente???


class Trace:
    """
    Classe per la descrizione delle tracce, ovvero le intersezioni (segmenti) tra i poligoni di un DFN
    """
    def __init__(self, parent1, parent2, i1, i2, estremi):
        """

        :param parent1, parent2: oggetti della classe Fracture, "genitori" della traccia
        :param i1, i2: indici di parent1 e parent2 all'interno della lista di tutte le fratture del DFN
        :param estremi: matrice (array di numpy di dimensione 2) 3 x 2, avente come colonne gli estremi della traccia
        """

        self.i1 = i1
        self.i2 = i2
        self.estremi = estremi
        self.parent1 = parent1
        self.parent2 = parent2

    def direzione(self):
        """

        :return: vettore direzione normalizzato (array di numpy di dimensione 1) della retta su cui giace la traccia
        """

        t = self.estremi[:, 1] - self.estremi[:, 0]
        t = t / np.linalg.norm(t)

        # O in alternativa:
        # t = np.cross(self.parent1.vn, self.parent2.vn)
        return t
