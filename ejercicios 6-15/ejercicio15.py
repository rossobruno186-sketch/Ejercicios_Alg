# Lista inicial de canciones de ejemplo
canciones = [
    {'nombre': 'Smells Like Teen Spirit', 'artista': 'Nirvana', 'anio': 1991},
    {'nombre': 'Paint It Black', 'artista': 'Rolling Stone', 'anio': 1966},
    {'nombre': 'Like a Stone', 'artista': 'Audioslave', 'anio': 2002},
    {'nombre': 'Come As You Are', 'artista': 'Nirvana', 'anio': 1991},
    {'nombre': 'Bohemian Rhapsody', 'artista': 'Queen', 'anio': 1975},
    {'nombre': 'Show Me How to Live', 'artista': 'Audioslave', 'anio': 2002}
]

def ordenar_por_nombre(lista):
    return sorted(lista, key=lambda x: x['nombre'])

def ordenar_por_artista(lista):
    return sorted(lista, key=lambda x: x['artista'])

def ordenar_por_anio(lista):
    return sorted(lista, key=lambda x: x['anio'])

def verificar_bandas(lista, bandas_a_buscar):
    """Verifica si existen canciones de las bandas indicadas."""
    encontradas = {banda: False for banda in bandas_a_buscar}
    
    for cancion in lista:
        if cancion['artista'] in encontradas:
            encontradas[cancion['artista']] = True
            
    return encontradas

def filtrar_por_artista(lista, artista_buscado):
    """Devuelve una lista solo con las canciones del artista indicado."""
    return [cancion for cancion in lista if cancion['artista'] == artista_buscado]

def agregar_y_ordenar(lista, nueva_cancion):
    """Agrega un diccionario a la lista y la devuelve ordenada por nombre."""
    lista.append(nueva_cancion)
    return ordenar_por_nombre(lista)

if __name__ == "__main__":
    print("=== A. LISTADOS ORDENADOS ===")
    
    print("\n-- Ordenado por Canción --")
    for c in ordenar_por_nombre(canciones):
        print(f"'{c['nombre']}' - {c['artista']} ({c['anio']})")
        
    print("\n-- Ordenado por Artista --")
    for c in ordenar_por_artista(canciones):
        print(f"{c['artista']} - '{c['nombre']}' ({c['anio']})")
        
    print("\n-- Ordenado por Año de lanzamiento --")
    for c in ordenar_por_anio(canciones):
        print(f"[{c['anio']}] '{c['nombre']}' - {c['artista']}")


    print("\n=== B. VERIFICAR AUDIOSLAVE Y ROLLING STONE ===")
    resultado_busqueda = verificar_bandas(canciones, ['Audioslave', 'Rolling Stone'])
    for banda, existe in resultado_busqueda.items():
        estado = "SÍ" if existe else "NO"
        print(f"¿Hay canciones de {banda}? {estado}")


    print("\n=== C. CANCIONES DE NIRVANA ===")
    canciones_nirvana = filtrar_por_artista(canciones, 'Nirvana')
    if canciones_nirvana:
        for c in canciones_nirvana:
            print(f"- {c['nombre']} ({c['anio']})")
    else:
        print("No se encontraron canciones de Nirvana.")


    print("\n=== D. AGREGAR CANCIÓN Y REORDENAR POR NOMBRE ===")
    nueva = {'nombre': 'Lithium', 'artista': 'Nirvana', 'anio': 1992}
    print(f"Agregando: '{nueva['nombre']}' de {nueva['artista']}...")
    
    lista_actualizada = agregar_y_ordenar(canciones, nueva)
    
    print("\n-- Nueva lista ordenada por Nombre --")
    for c in lista_actualizada:
        print(f"'{c['nombre']}' - {c['artista']} ({c['anio']})")