from super_heroes_data import superheroes

# Tomar los primeros 15 superhéroes
primeros_15 = superheroes[:15]

# 1. Función recursiva para determinar si Capitán América está en la lista
def buscar_capitan_america(lista, indice=0):
    # Caso base: Si llegamos al final de la lista sin encontrarlo
    if indice == len(lista):
        return False
    
    # Caso base: Si encontramos a Capitán América (buscamos por 'name')
    nombre = lista[indice].get("name", "")
    if nombre == "Captain America" or nombre == "Capitan America":
        return True
    
    # Llamada recursiva con el siguiente índice
    return buscar_capitan_america(lista, indice + 1)

# 2. Función recursiva para listar los superhéroes de la lista
def listar_superheroes(lista, indice=0):
    # Caso base: Si llegamos al final de la lista, terminamos
    if indice == len(lista):
        return
    
    # Acción: Imprimir el nombre del superhéroe actual
    print(f"{indice + 1}. {lista[indice].get('name')}")
    
    # Llamada recursiva con el siguiente índice
    listar_superheroes(lista, indice + 1)

# Ejecución de prueba
if __name__ == "__main__":
    print("--- Listando los primeros 15 superhéroes de la lista proporcionada por walter ---")
    listar_superheroes(primeros_15)
    
    print("\n--- ¿Está el Capitán América en la lista de los primeros 15? ---")
    encontrado = buscar_capitan_america(primeros_15)
    if encontrado:
        print("Sí, el Capitán América está en la lista.")
    else:
        print("No, el Capitán América NO está en la lista.")
