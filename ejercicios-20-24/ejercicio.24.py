from stack import Stack

def resolver_actividades(pila):
    pos_rocket = -1
    pos_groot = -1
    posicion_actual = 1  
    
    personajes_mas_5_peliculas = []
    
    peliculas_black_widow = 0
    
    personajes_c_d_g = []
    
    pila_aux = Stack()
    
    while pila.size() > 0:
        personaje = pila.pop()
        nombre = personaje['nombre']
        peliculas = personaje['peliculas']
        
        if nombre == 'Rocket Raccoon':
            pos_rocket = posicion_actual
        elif nombre == 'Groot':
            pos_groot = posicion_actual
            
        if peliculas > 5:
            personajes_mas_5_peliculas.append((nombre, peliculas))
            
        if nombre == 'Black Widow':
            peliculas_black_widow = peliculas
            
        if nombre.startswith('C') or nombre.startswith('D') or nombre.startswith('G'):
            personajes_c_d_g.append(nombre)
            
        posicion_actual += 1
        
        pila_aux.push(personaje)
        
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
        
    print("--- RESULTADOS DEL EJERCICIO 24 ---")
    
    print(f"\na. Posición de Rocket Raccoon: {pos_rocket if pos_rocket != -1 else 'No se encontró'}")
    print(f"   Posición de Groot: {pos_groot if pos_groot != -1 else 'No se encontró'}")
    
    print("\nb. Personajes con más de 5 películas:")
    for nombre, cant in personajes_mas_5_peliculas:
        print(f"   - {nombre} ({cant} películas)")
        
    print(f"\nc. Black Widow participó en {peliculas_black_widow} películas.")
    
    print("\nd. Personajes cuyos nombres empiezan con C, D o G:")
    for nombre in personajes_c_d_g:
        print(f"   - {nombre}")

if __name__ == "__main__":
    pila_mcu = Stack()
    
    personajes_datos = [
        {'nombre': 'Iron Man', 'peliculas': 10},
        {'nombre': 'Capitán América', 'peliculas': 9},
        {'nombre': 'Hulk', 'peliculas': 7},
        {'nombre': 'Thor', 'peliculas': 8},
        {'nombre': 'Black Widow', 'peliculas': 8},
        {'nombre': 'Daredevil', 'peliculas': 0},
        {'nombre': 'Doctor Strange', 'peliculas': 4},
        {'nombre': 'Gamora', 'peliculas': 4},
        {'nombre': 'Ghost Rider', 'peliculas': 2},
        {'nombre': 'Rocket Raccoon', 'peliculas': 5},
        {'nombre': 'Groot', 'peliculas': 5}
    ]

    for p in personajes_datos:
        pila_mcu.push(p)

    resolver_actividades(pila_mcu)
