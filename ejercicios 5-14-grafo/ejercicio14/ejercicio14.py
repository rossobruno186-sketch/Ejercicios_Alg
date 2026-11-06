from graph import Graph

def resolver_red_casa():

    casa = Graph(is_dir=False)

    ambientes = [
        "cocina", "comedor", "cochera", "quincho", 
        "baño 1", "baño 2", "habitación 1", 
        "habitación 2", "sala de estar", "terraza", "patio"
    ]

    for ambiente in ambientes:
        casa.add_vertex(ambiente)

    conexiones = [
        (10, "cocina", "comedor"), (5, "cocina", "baño 1"), (15, "cocina", "patio"),
        (8, "comedor", "sala de estar"), (12, "comedor", "habitación 1"), 
        (4, "comedor", "baño 2"), (14, "comedor", "terraza"),
        (20, "cochera", "patio"), (10, "cochera", "quincho"), (18, "cochera", "habitación 2"),
        (8, "quincho", "patio"), (12, "quincho", "terraza"),
        (6, "baño 1", "habitación 1"), (7, "baño 1", "habitación 2"),
        (5, "baño 2", "habitación 1"), (3, "baño 2", "sala de estar"),
        (4, "habitación 1", "habitación 2"), (15, "habitación 2", "terraza"),
        (7, "sala de estar", "terraza"), (9, "terraza", "patio")
    ]

    for peso, origen, destino in conexiones:
        casa.add_edge(peso, origen, destino)

    print("--- c. Árbol de Expansión Mínima ---")
    arbol_minimo = casa.kruskal("cocina")
    
    metros_totales = 0
    print("Conexiones necesarias para cablear todos los ambientes:")
    if isinstance(arbol_minimo, str):
        for arista in arbol_minimo.split(';'):
            origen, destino, peso = arista.split('-')
            print(f" - De {origen} a {destino} ({peso} metros)")
            metros_totales += int(peso)
            
    print(f"\nTotal de cable eléctrico necesario: {metros_totales} metros\n")

    print("--- d. Cable de red desde router (hab 1) a Smart TV (sala) ---")
    
    caminos_stack = casa.dijkstra("habitación 1")
    
    destino_final = "sala de estar"
    destino_actual = destino_final
    peso_total_red = None
    ruta_red = []

    while caminos_stack.size() > 0:
        valor = caminos_stack.pop() 
        
        if valor[0] == destino_actual:
            if peso_total_red is None:
                peso_total_red = valor[1] 
            ruta_red.append(valor[0])
            destino_actual = valor[2] 
            
    ruta_red.reverse()
    
    print(f"Ruta óptima del cable de red: {' -> '.join(ruta_red)}")
    print(f"Metros de cable de red necesarios: {peso_total_red} metros")

if __name__ == "__main__":
    resolver_red_casa()