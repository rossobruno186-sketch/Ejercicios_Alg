from super_heroes_data import superheroes

primeros_15 = superheroes[:15]

def buscar_capitan_america(lista, indice=0):
    # Caso base: Si llegamos al final de la lista sin encontrarlo
    if indice == len(lista):
        return False
    
    nombre = lista[indice].get("name", "")
    if nombre == "Captain America" or nombre == "Capitan America":
        return True
    
    return buscar_capitan_america(lista, indice + 1)

def listar_superheroes(lista, indice=0):
    if indice == len(lista):
        return
    
    print(f"{indice + 1}. {lista[indice].get('name')}")
    
    listar_superheroes(lista, indice + 1)

if __name__ == "__main__":
    print("--- Listando los primeros 15 superhéroes de la lista proporcionada por walter ---")
    listar_superheroes(primeros_15)
    
    print("\n--- ¿Está el Capitán América en la lista de los primeros 15? ---")
    encontrado = buscar_capitan_america(primeros_15)
    if encontrado:
        print("Sí, el Capitán América está en la lista.")
    else:
        print("No, el Capitán América NO está en la lista.")
