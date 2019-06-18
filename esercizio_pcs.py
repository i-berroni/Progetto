import networkx as nx
import matplotlib.pyplot as plt


def visita_profondita(grafo, vertice_start, plot_grafo=False, plot_albero=False, plot_anim=False):
    """
    Visita in profondita' di un grafo con albero di ricoprimento

    :param grafo: deve essere un grafo di networkx
    :param vertice_start: nodo arbitrario del grafo
    :param plot_grafo: booleano che indica se visualizzare il grafo da visitare
    :param plot_albero: booleano che indica se visualizzare l'albero di ricoprimento del grafo
    :param plot_anim: booleano che indica se visualizzare l'animazione della visita del grafo
    :return: albero di ricoprimento della visita
    """

    albero = nx.Graph()
    nodi_da_visitare = []
    nodi_da_visitare.append(vertice_start)

    pos = nx.spring_layout(grafo)

    # Le due liste "nodi_scoperti" e "nodi_non_scoperti" servono per l'animazione della visita
    if plot_anim is True:
        nodi_scoperti = [vertice_start]
        nodi_non_scoperti = list(grafo.nodes())
        nodi_non_scoperti.remove(vertice_start)

    for v in grafo.nodes():
        if v != vertice_start:
            grafo.nodes[v]['colore'] = 'blu'  # blu -> non scoperto

    grafo.nodes[vertice_start]['colore'] = 'verde'  # verde -> scoperto
    albero.add_node(vertice_start)

    plt.axes().clear()
    while len(nodi_da_visitare) > 0:

        v_green = nodi_da_visitare.pop()  # la mia struttura dati e' una pila: rimuovo l'ultimo elemento inserito

        for v in list(grafo[v_green]):

            if plot_anim is True:
                nx.draw_networkx(grafo, pos, nodelist=nodi_non_scoperti, node_color='b')
                nx.draw_networkx(grafo, pos, nodelist=nodi_scoperti, node_color='g')
                plt.pause(0.2)
                plt.axes().clear()

            if grafo.nodes[v]['colore'] != 'verde':
                nodi_da_visitare.append(v)
                grafo.nodes[v]['colore'] = 'verde'
                albero.add_node(v)
                albero.add_edge(v_green, v)
                if plot_anim is True:
                    nodi_non_scoperti.remove(v)
                    nodi_scoperti.append(v)

    if plot_grafo is True:
        nx.draw_networkx(grafo, pos)
        plt.pause(2)
        plt.axes().clear()

    if plot_albero is True:
        nx.draw_networkx(albero, pos)
        plt.pause(2)
        plt.axes().clear()

    return albero


def visita_ampiezza(grafo, vertice_start, plot_grafo=False, plot_albero=False, plot_anim=False):
    """
    Visita in ampiezza di un grafo con albero di ricoprimento

    :param grafo: deve essere un grafo di networkx
    :param vertice_start: nodo arbitrario del grafo
    :param plot_grafo: booleano che indica se visualizzare il grafo da visitare
    :param plot_albero: booleano che indica se visualizzare l'albero di ricoprimento del grafo
    :param plot_anim: booleano che indica se visualizzare l'animazione della visita del grafo
    :return: albero di ricoprimento della visita
    """

    albero = nx.Graph()
    nodi_da_visitare = []
    nodi_da_visitare.append(vertice_start)

    pos = nx.spring_layout(grafo)

    # Le due liste "nodi_scoperti" e "nodi_non_scoperti" servono per l'animazione della visita
    if plot_anim is True:
        nodi_scoperti = [vertice_start]
        nodi_non_scoperti = list(grafo.nodes())
        nodi_non_scoperti.remove(vertice_start)

    for v in grafo.nodes():
        if v != vertice_start:
            grafo.nodes[v]['colore'] = 'blu'  # blu -> non scoperto

    grafo.nodes[vertice_start]['colore'] = 'verde'  # verde -> scoperto
    albero.add_node(vertice_start)

    plt.axes().clear()
    while len(nodi_da_visitare) > 0:

        v_green = nodi_da_visitare.pop(0)  # la mia struttura dati e' una coda: rimuovo il primo elemento inserito

        for v in list(grafo[v_green]):

            if plot_anim is True:
                nx.draw_networkx(grafo, pos, nodelist=nodi_non_scoperti, node_color='b')
                nx.draw_networkx(grafo, pos, nodelist=nodi_scoperti, node_color='g')
                plt.pause(0.2)
                plt.axes().clear()

            if grafo.nodes[v]['colore'] != 'verde':
                nodi_da_visitare.append(v)
                grafo.nodes[v]['colore'] = 'verde'
                albero.add_node(v)
                albero.add_edge(v_green, v)
                if plot_anim is True:
                    nodi_non_scoperti.remove(v)
                    nodi_scoperti.append(v)

    if plot_grafo is True:
        nx.draw_networkx(grafo, pos)
        plt.pause(2)
        plt.axes().clear()

    if plot_albero is True:
        nx.draw_networkx(albero, pos)
        plt.pause(2)
        plt.axes().clear()

    return albero

