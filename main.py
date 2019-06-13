import numpy as np
import DFN as dfn

# Settiamo i parametri del costruttore del DFN

N = 5
Xmin = 0
Xmax = 5
Ymin = 0
Ymax = 5
Zmin = 0
Zmax = 5
alpha_pl = 2
radius_l = 2
radius_u = 3
k = 3
mode_vector = np.array([[0.], [0.], [1.]])
fixed_n_edges = 0

# Creiamo un network

network = dfn.DiscreteFractureNetwork(N, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax,
                                      alpha_pl, radius_l, radius_u, k, mode_vector, fixed_n_edges)
v = [1, 4]
#network.visual3D('1')
network.scrittura1()
network.scrittura2()
network.rimuovi(v)
network.scrittura1('file3.txt')
network.scrittura2('file4.txt')
network.visual3D('2')
