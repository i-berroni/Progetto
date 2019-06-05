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

        """

        self.i1 = i1
        self.i2 = i2
        self.estremi = estremi
        self.parent1 = parent1
        self.parent2 = parent2


    def direzione(self):
        """

        :return:
        """