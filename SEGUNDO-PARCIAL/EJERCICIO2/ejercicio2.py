from graph import Graph

g = Graph(is_dir=False)

personajes = [
    ("Luke Skywalker", 6), ("Darth Vader", 6), ("Yoda", 6), 
    ("Boba Fett", 3), ("C-3PO", 9), ("Leia", 7), 
    ("Rey", 3), ("Kylo Ren", 3), ("Chewbacca", 8), 
    ("Han Solo", 5), ("R2-D2", 9), ("BB-8", 3)
]

for nombre, eps in personajes:
    g.add_vertex(nombre, other_values={'episodes': eps})

aristas = [
    ("Luke Skywalker", "Darth Vader", 3),
    ("Luke Skywalker", "Leia", 5),
    ("Luke Skywalker", "R2-D2", 6),
    ("Luke Skywalker", "C-3PO", 6),
    ("Luke Skywalker", "Yoda", 3),
    ("Darth Vader", "Yoda", 1),
    ("Leia", "Han Solo", 4),
    ("Han Solo", "Chewbacca", 5),
    ("R2-D2", "C-3PO", 9),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Chewbacca", "Yoda", 1),
    ("Leia", "C-3PO", 6),
    ("Yoda", "C-3PO", 3)
]

for origen, destino, peso in aristas:
    g.add_edge(peso, origen, destino)

print("=== EJERCICIO 2: GRAFO DE STAR WARS ===\n")

print("--- ÁRBOL DE EXPANSIÓN MÍNIMO (Kruskal) ---")
for origen in ["C-3PO", "Yoda", "Leia"]:
    print(f"\nDesde {origen}:")
    mst = g.kruskal(origen)
    print(mst)

print("\n--- MÁXIMO DE EPISODIOS COMPARTIDOS ---")
max_eps = 0
pares_maximos = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_eps:
            max_eps = edge.weight
            pares_maximos = [tuple(sorted([vertex.value, edge.destination]))]
        elif edge.weight == max_eps:
            par = tuple(sorted([vertex.value, edge.destination]))
            if par not in pares_maximos:
                pares_maximos.append(par)

print(f"Máximo de episodios compartidos: {max_eps}")
for par in pares_maximos:
    print(f"Pares: {par[0]} y {par[1]}")

def calcular_camino(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        return None, 0
        
    paths = grafo.dijkstra(origen)
    peso_total = None
    camino_completo = []
    
    current_dest = destino
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == current_dest:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            current_dest = value[2]
            
    camino_completo.reverse()
    return camino_completo, peso_total

print("\n--- CAMINOS MÁS CORTOS (Dijkstra) ---")
camino1, costo1 = calcular_camino(g, "C-3PO", "R2-D2")
print(f"De C-3PO a R2-D2: {' -> '.join(camino1)} (Total episodios juntos en el trayecto: {costo1})")

camino2, costo2 = calcular_camino(g, "Yoda", "Darth Vader")
print(f"De Yoda a Darth Vader: {' -> '.join(camino2)} (Total episodios juntos en el trayecto: {costo2})")

print("\n--- PERSONAJES EN LOS 9 EPISODIOS ---")
para_los_9 = []
for vertex in g:
    if vertex.other_values and vertex.other_values.get('episodes') == 9:
        para_los_9.append(vertex.value)

if para_los_9:
    print(f"Los personajes que aparecieron en toda la saga (9 episodios) son: {', '.join(para_los_9)}")
else:
    print("Ningún personaje apareció en los 9 episodios.")