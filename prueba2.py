import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, madera, caja, tiempo_secado, cantidad_madera):
        self.madera = madera
        self.caja = caja
        self.tiempo_secado = tiempo_secado
        self.cantidad_madera = cantidad_madera
        self.siguiente = None

def insertar_nodo(lista, nodo):
    if lista is None:
        return nodo
    if nodo.tiempo_secado > lista.tiempo_secado:
        nodo.siguiente = lista
        return nodo
    temp = lista
    while temp.siguiente is not None and temp.siguiente.tiempo_secado > nodo.tiempo_secado:
        temp = temp.siguiente
    nodo.siguiente = temp.siguiente
    temp.siguiente = nodo
    return lista

def mostrar_nodos(lista):
    while lista is not None:
        print(f"{lista.madera} - Caja {lista.caja}: {lista.tiempo_secado} días, Cantidad de madera: {lista.cantidad_madera}")
        lista = lista.siguiente

def visualizar_grafico(lista):
    G = nx.Graph()

    while lista is not None:
        G.add_node(f"{lista.madera} - Caja {lista.caja}", tiempo_secado=lista.tiempo_secado, cantidad_madera=lista.cantidad_madera)
        if lista.siguiente is not None:
            G.add_edge(f"{lista.madera} - Caja {lista.caja}", f"{lista.siguiente.madera} - Caja {lista.siguiente.caja}")
        lista = lista.siguiente

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'tiempo_secado')

    nx.draw(G, pos, with_labels=True, font_size=8, font_color='black', font_weight='bold', node_color='skyblue', edge_color='gray', alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Gráfico de nodos ordenados por tiempo de secado")
    plt.show()

# Datos de madera, tiempo de secado y cantidad de madera
maderas = ["Nogal", "Castaño", "Pino", "Abedul", "Roble"]
cantidad_cajas = 3

# Crear nodos y organizar la lista
lista_nodos = None
for madera in maderas:
    for caja in range(1, cantidad_cajas + 1):
        tiempo_secado = int(input(f"Ingrese el tiempo de secado para {madera} - Caja {caja}: "))
        cantidad_madera = int(input(f"Ingrese la cantidad de madera para {madera} - Caja {caja}: "))
        lista_nodos = insertar_nodo(lista_nodos, Nodo(madera, caja, tiempo_secado, cantidad_madera))

# Mostrar nodos ordenados
print("\nNodos ordenados por tiempo de secado:")
mostrar_nodos(lista_nodos)

# Visualizar gráfico de nodos
visualizar_grafico(lista_nodos)