from graph import Graph

def resolver_red():
    red = Graph(is_dir=False)

    nodos = [
        ("Ubuntu", "pc"),
        ("Mint", "pc"),
        ("Manjaro", "pc"),
        ("Parrot", "pc"),
        ("Fedora", "pc"),
        ("Debian", "notebook"),
        ("Red Hat", "notebook"),
        ("Arch", "notebook"),
        ("Guaraní", "servidor"),
        ("MongoDB", "servidor"),
        ("Router 1", "router"),
        ("Router 2", "router"),
        ("Router 3", "router"),
        ("Switch 1", "switch"),
        ("Switch 2", "switch"),
        ("Impresora", "impresora")
    ]

    for nombre, tipo in nodos:
        red.add_vertex(nombre, tipo)

    aristas = [
        (17, "Debian", "Switch 1"),
        (18, "Ubuntu", "Switch 1"),
        (22, "Impresora", "Switch 1"),
        (80, "Mint", "Switch 1"),
        (29, "Switch 1", "Router 1"),
        (37, "Router 1", "Router 2"),
        (43, "Router 1", "Router 3"),
        (50, "Router 2", "Router 3"),
        (25, "Red Hat", "Router 2"),
        (9, "Guaraní", "Router 2"),
        (61, "Router 3", "Switch 2"),
        (40, "Manjaro", "Switch 2"),
        (12, "Parrot", "Switch 2"),
        (3, "Fedora", "Switch 2"),
        (56, "Arch", "Switch 2"),
        (5, "MongoDB", "Switch 2")
    ]

    for peso, origen, destino in aristas:
        red.add_edge(peso, origen, destino)

    print("--- b. Barrido DFS y BFS ---")
    for notebook in ["Red Hat", "Debian", "Arch"]:
        print(f"\nProfundidad (DFS) desde {notebook}:")
        red.deep_show(notebook)
        print(f"\nAmplitud (BFS) desde {notebook}:")
        red.amplitude_show(notebook)

    def obtener_camino_corto(grafo, origen, destino):
        caminos = grafo.dijkstra(origen)
        peso_total = None
        camino_completo = []
        destino_actual = destino
        
        while caminos.size() > 0:
            valor = caminos.pop()
            if valor[0] == destino_actual:
                if peso_total is None:
                    peso_total = valor[1]
                camino_completo.append(valor[0])
                destino_actual = valor[2]
        
        camino_completo.reverse()
        return camino_completo, peso_total

    print("\n--- c. Camino más corto a la Impresora ---")
    for pc in ["Manjaro", "Red Hat", "Fedora"]:
        camino, costo = obtener_camino_corto(red, pc, "Impresora")
        print(f"Desde {pc}: {' -> '.join(camino)} (Costo: {costo})")

    print("\n--- d. Árbol de Expansión Mínima ---")
    arbol_minimo = red.kruskal("Router 1")
    print(arbol_minimo)

    print("\n--- e. PC más cercana a Guaraní ---")
    pcs = ["Ubuntu", "Mint", "Manjaro", "Parrot", "Fedora"]
    min_costo_guarani = float('inf')
    pc_mas_cercana = ""

    for pc in pcs:
        camino, costo = obtener_camino_corto(red, pc, "Guaraní")
        if costo is not None and costo < min_costo_guarani:
            min_costo_guarani = costo
            pc_mas_cercana = pc
    print(f"La PC con el camino más corto a Guaraní es {pc_mas_cercana} con un costo de {min_costo_guarani}")

    print("\n--- f. Computadora del Switch 1 más cercana a MongoDB ---")
    computadoras_sw1 = ["Debian", "Ubuntu", "Mint"] 
    min_costo_mongo = float('inf')
    comp_mas_cercana = ""

    for comp in computadoras_sw1:
        camino, costo = obtener_camino_corto(red, comp, "MongoDB")
        if costo is not None and costo < min_costo_mongo:
            min_costo_mongo = costo
            comp_mas_cercana = comp
    print(f"La computadora del Switch 1 con el camino más corto a MongoDB es {comp_mas_cercana} con un costo de {min_costo_mongo}")

    print("\n--- g. Cambiar conexión de Impresora a Router 2 y re-ejecutar barridos ---")
    red.delete_edge("Impresora", "Switch 1")
    red.add_edge(22, "Impresora", "Router 2") 

    for notebook in ["Red Hat", "Debian", "Arch"]:
        print(f"\nProfundidad (DFS) desde {notebook} (Nueva conexión):")
        red.deep_show(notebook)
        print(f"\nAmplitud (BFS) desde {notebook} (Nueva conexión):")
        red.amplitude_show(notebook)


if __name__ == "__main__":
    resolver_red()