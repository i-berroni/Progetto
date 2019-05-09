import networkx as nx
import matplotlib.pyplot as plt

# Che colori usare? Dovrebbe servire solo un colore per "scoperto" (verde) e uno per "non scoperto" (blu)

# NON FUNZIONA IL PLOT DEI GRAFI QUANDO I PARAMETRI SONO SETTATI COME TRUE, NONOSTANTE IL COMANDO SIA CORRETTO

# E' DA IMPLEMENTARE ANCORA LA POSSIBILITA' DI VEDERE UN'ANIMAZIONE DELLA VISITA DEL GRAFO


def visita_profondita(grafo, vertice_start, plot_grafo=False, plot_albero=False):
    """
    Visita in profondita' di un grafo con albero di ricoprimento

    :param grafo: deve essere un grafo di networkx
    :param vertice_start: nodo arbitrario del grafo
    :return: albero di ricoprimento della visita
    """

    albero = nx.Graph()
    nodi_da_visitare = []
    nodi_da_visitare.append(vertice_start)

    for v in grafo.nodes():
        if v != vertice_start:
            grafo.nodes[v]['colore'] = 'blu'  # blu -> non scoperto

    grafo.nodes[vertice_start]['colore'] = 'verde'  # verde -> scoperto
    albero.add_node(vertice_start)

    while len(nodi_da_visitare) > 0:
        v_green = nodi_da_visitare.pop()  # la mia struttura dati e' una pila: rimuovo l'ultimo elemento inserito
        for v in list(grafo[v_green]):
            if grafo.nodes[v]['colore'] != 'verde':
                nodi_da_visitare.append(v)
                grafo.nodes[v]['colore'] = 'verde'
                albero.add_node(v)
                albero.add_edge(v_green, v)

    if plot_grafo is True:
        nx.draw_networkx(grafo)
    if plot_albero is True:
        nx.draw_networkx(albero)

    return albero

def visita_ampiezza(grafo, vertice_start, plot_grafo=False, plot_albero=False):
    """
    Visita in profondita' di un grafo con albero di ricoprimento

    :param grafo: deve essere un grafo di networkx
    :param vertice_start: nodo arbitrario del grafo
    :return: albero di ricoprimento della visita
    """

    albero = nx.Graph()
    nodi_da_visitare = []
    nodi_da_visitare.append(vertice_start)

    for v in grafo.nodes():
        if v != vertice_start:
            grafo.nodes[v]['colore'] = 'blu'  # blu -> non scoperto

    grafo.nodes[vertice_start]['colore'] = 'verde'  # verde -> scoperto
    albero.add_node(vertice_start)

    while len(nodi_da_visitare) > 0:
        v_green = nodi_da_visitare.pop(0)  # la mia struttura dati e' una coda: rimuovo il primo elemento inserito (rimasto nella coda)
        for v in list(grafo[v_green]):
            if grafo.nodes[v]['colore'] != 'verde':
                nodi_da_visitare.append(v)
                grafo.nodes[v]['colore'] = 'verde'
                albero.add_node(v)
                albero.add_edge(v_green, v)

    if plot_grafo is True:
        nx.draw_networkx(grafo)
    if plot_albero is True:
        nx.draw_networkx(albero)

    return albero


grafo_test = nx.Graph()
grafo_test.add_nodes_from('ABCDEFGHILMN')
grafo_test.add_edges_from(('AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IL', 'LA', 'MA', 'MD', 'MN', 'BL', 'CI', 'IG', 'NF', 'NH'))

albero_ricoprimento1 = visita_ampiezza(grafo_test, 'A', True, True)
albero_ricoprimento2 = visita_profondita(grafo_test, 'A', True, True)
print(albero_ricoprimento1.nodes)
print(albero_ricoprimento1.edges)
print(albero_ricoprimento2.nodes)
print(albero_ricoprimento2.edges)
print(grafo_test.nodes)
print(grafo_test.edges)
