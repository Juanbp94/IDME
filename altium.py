# Esquemático del Arduino Nano
# Representación de los componentes y conexiones en un circuito

import matplotlib.pyplot as plt
import networkx as nx

def draw_schematic():
    G = nx.DiGraph()
    
    # Añadir nodos (componentes principales)
    components = {
        "USB": (0, 3),
        "CH340G": (2, 3),
        "Regulador 5V": (4, 3),
        "Regulador 3.3V": (6, 3),
        "ATmega328P": (3, 2),
        "Cristal 16MHz": (3, 1),
        "LED Power": (5, 1),
        "Botón Reset": (1, 1),
        "Pines I/O": (3, 0)
    }
    
    for component, pos in components.items():
        G.add_node(component, pos=pos)
    
    # Añadir conexiones entre componentes
    connections = [
        ("USB", "CH340G"),
        ("CH340G", "ATmega328P"),
        ("Regulador 5V", "ATmega328P"),
        ("Regulador 3.3V", "ATmega328P"),
        ("Cristal 16MHz", "ATmega328P"),
        ("LED Power", "Regulador 5V"),
        ("Botón Reset", "ATmega328P"),
        ("ATmega328P", "Pines I/O")
    ]
    
    G.add_edges_from(connections)
    
    # Dibujar el gráfico
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', edge_color='gray', font_size=8, font_weight='bold')
    plt.title("Esquemático del Arduino Nano")
    plt.show()

draw_schematic()
