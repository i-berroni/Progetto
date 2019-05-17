import esercizio_pcs as es
import networkx as nx

# Ricostruiamo il grafo delle slide per testare le funzioni

grafo_test = nx.Graph()
grafo_test.add_nodes_from('ABCDEFGHILMN')
grafo_test.add_edges_from(('AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IL',
                           'LA', 'MA', 'MD', 'MN', 'BL', 'CI', 'IG', 'NF', 'NH'))

albero_ricoprimento1 = es.visita_ampiezza(grafo_test, 'A', plot_albero=True, plot_grafo=True, plot_anim=True)
albero_ricoprimento2 = es.visita_profondita(grafo_test, 'A', plot_albero=True, plot_grafo=True, plot_anim=True)

# print(albero_ricoprimento1.nodes)
# print(albero_ricoprimento1.edges)
# print(albero_ricoprimento2.nodes)
# print(albero_ricoprimento2.edges)
# print(grafo_test.nodes)
# print(grafo_test.edges)

