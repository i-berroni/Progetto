import networkx as nx

# Ricostruiamo il grafo delle slide per testare le funzione
grafo_test = nx.Graph()
grafo_test.add_nodes_from('ABCDEFGHILMN')
grafo_test.add_edges_from(('AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IL', 'LA', 'MA', 'MD', 'MN', 'BL', 'CI', 'IG', 'NF', 'NH'))

# Come modificare attributi di un grafo
petersen = nx.petersen_graph()
petersen.nodes[0]['colore'] = 'rosso'
petersen.nodes[0]['valore'] = 1.5
petersen.nodes[0] # mi dà attributo e valore
