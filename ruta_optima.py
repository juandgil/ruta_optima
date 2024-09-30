import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def crear_grafo():
    # Crear un grafo
    G = nx.Graph()

    # Añadir nodos (lugares cerca de Medellín)
    nodos = ["medellin", "bello", "envigado", "sabaneta", "itagui"]
    G.add_nodes_from(nodos)

    # Añadir aristas con pesos (distancias en kilómetros)
    aristas = [("medellin", "bello", 10), ("medellin", "envigado", 10), 
               ("bello", "itagui", 15), ("envigado", "itagui", 8), 
               ("envigado", "sabaneta", 5), ("itagui", "sabaneta", 4)]
    G.add_weighted_edges_from(aristas)

    return G

def calcular_ruta(G, inicio, fin):
    # Encontrar la ruta más corta
    ruta = nx.shortest_path(G, inicio, fin, weight="weight")
    distancia = nx.shortest_path_length(G, inicio, fin, weight="weight")

    # Imprimir los resultados
    print(f"La ruta más corta de {inicio} a {fin} es: {' -> '.join(ruta)}")
    print(f"La distancia total es: {distancia} km")

    return ruta, distancia

def visualizar_grafo(G, ruta):
    # Limpiar la figura anterior
    plt.clf()

    # Dibujar el grafo
    posicion = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, posicion, node_color='lightblue', node_size=3000)
    nx.draw_networkx_edges(G, posicion)
    nx.draw_networkx_labels(G, posicion, font_size=8)
    etiquetas_aristas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posicion, edge_labels=etiquetas_aristas)

    # Resaltar la ruta más corta
    aristas_ruta = list(zip(ruta, ruta[1:]))
    nx.draw_networkx_edges(G, posicion, edgelist=aristas_ruta, edge_color='r', width=2)

    # Configurar y mostrar el gráfico
    plt.title("Grafo con la ruta más corta resaltada")
    plt.axis('off')
    plt.show()

def calcular_y_mostrar_ruta():
    inicio = entrada_inicio.get().lower().strip()
    fin = entrada_fin.get().lower().strip()
    
    if inicio not in G.nodes() or fin not in G.nodes():
        messagebox.showerror("Error", "Lugares de inicio o fin no válidos.\nLugares válidos: medellin, bello, envigado, sabaneta, itagui")
        return

    ruta, _ = calcular_ruta(G, inicio, fin)
    visualizar_grafo(G, ruta)

# Crear el grafo
G = crear_grafo()

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Ruta Óptima en el Área Metropolitana de Medellín")

# Entrada para el punto de inicio
tk.Label(ventana, text="Lugar de inicio:").grid(row=0, column=0)
entrada_inicio = tk.Entry(ventana)
entrada_inicio.grid(row=0, column=1)

# Entrada para el punto final
tk.Label(ventana, text="Lugar final:").grid(row=1, column=0)
entrada_fin = tk.Entry(ventana)
entrada_fin.grid(row=1, column=1)

# Botón para calcular la ruta
boton_calcular = tk.Button(ventana, text="Calcular Ruta", command=calcular_y_mostrar_ruta)
boton_calcular.grid(row=2, column=0, columnspan=2)

# Mostrar lugares válidos
lugares_validos = "Lugares válidos: medellin, bello, envigado, sabaneta, itagui"
tk.Label(ventana, text=lugares_validos).grid(row=3, column=0, columnspan=2)

ventana.mainloop()