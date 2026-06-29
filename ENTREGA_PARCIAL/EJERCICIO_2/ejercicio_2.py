from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

class SuperHero:
    def __init__(self, data):
        self.name = data.get("name", "")
        self.alias = data.get("alias", "")
        self.real_name = data.get("real_name") or ""
        self.bio = data.get("short_bio", "")
        self.first_appearance = data.get("first_appearance")
        self.is_villain = data.get("is_villain", False)

    def __str__(self):
        return f"Nombre: {self.name} | Real: {self.real_name} | Aparición: {self.first_appearance} | Villano: {self.is_villain}"

def print_separator(title):
    print(f"\n{'='*10} {title} {'='*10}")

def main():
    # Inicializar la lista personalizada con los datos importados
    lista_heroes = List()
    for sh_data in superheroes:
        lista_heroes.append(SuperHero(sh_data))
    
    # Añadir criterios de ordenamiento y búsqueda
    lista_heroes.add_criterion('name', lambda x: x.name)
    lista_heroes.add_criterion('real_name', lambda x: x.real_name)
    lista_heroes.add_criterion('first_appearance', lambda x: x.first_appearance if x.first_appearance is not None else 9999)

    # 1. Listado ordenado de manera ascendente por nombre de los personajes.
    print_separator("1. Listado ordenado de manera ascendente por nombre")
    lista_heroes.sort_by_criterion('name')
    lista_heroes.show()

    # 2. Determinar en que posicion esta The Thing y Rocket Raccoon.
    print_separator("2. Posición de The Thing y Rocket Raccoon")
    pos_thing = lista_heroes.search("The Thing", "name")
    pos_rocket = lista_heroes.search("Rocket Raccoon", "name")
    
    print(f"The Thing se encuentra en el índice/posición: {pos_thing}")
    print(f"Rocket Raccoon se encuentra en el índice/posición: {pos_rocket}")

    # 3. Listar todos los villanos de la lista.
    print_separator("3. Todos los villanos de la lista")
    for h in lista_heroes:
        if h.is_villain:
            print(h.name)

    # 4. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
    print_separator("4. Villanos en cola que aparecieron antes de 1980")
    cola_villanos = Queue()
    for h in lista_heroes:
        if h.is_villain:
            cola_villanos.arrive(h)
    
    while cola_villanos.size() > 0:
        v = cola_villanos.attention()
        if v.first_appearance is not None and v.first_appearance < 1980:
            print(f"{v.name} (Aparición: {v.first_appearance})")

    # 5. Listar los superheores que comienzan con Bl, G, My, y W.
    print_separator("5. Superhéroes que comienzan con Bl, G, My, y W")
    lista_heroes.filter_start_with(("Bl", "G", "My", "W"))

    # 6. Listado de personajes ordenado por nombre real de manera ascendente.
    print_separator("6. Listado ordenado por nombre real de manera ascendente")
    lista_heroes.sort_by_criterion('real_name')
    lista_heroes.show()

    # 7. Listado de superheroes ordenados por fecha de aparación.
    print_separator("7. Listado ordenado por fecha de aparición")
    lista_heroes.sort_by_criterion('first_appearance')
    lista_heroes.show()

    # 8. Modificar el nombre real de Ant Man a Scott Lang.
    print_separator("8. Modificar el nombre real de Ant Man")
    index_ant_man = lista_heroes.search("Ant Man", "name")
    if index_ant_man is not None:
        lista_heroes[index_ant_man].real_name = "Scott Lang"
        print(f"Modificado exitosamente. Ant Man ahora tiene el nombre real: {lista_heroes[index_ant_man].real_name}")

    # 9. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
    print_separator("9. Personajes con 'time-traveling' o 'suit' en su biografía")
    lista_heroes.filter_contain_on_bio(("time-traveling", "suit"))

    # 10. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
    print_separator("10. Eliminar a Electro y Baron Zemo")
    electro = lista_heroes.delete_value("Electro", "name")
    if electro:
        print(f"Se ha eliminado a Electro. Información: {electro}")
    else:
        print("Electro no estaba en la lista.")

    zemo = lista_heroes.delete_value("Baron Zemo", "name")
    if zemo:
        print(f"Se ha eliminado a Baron Zemo. Información: {zemo}")
    else:
        print("Baron Zemo no estaba en la lista.")

if __name__ == "__main__":
    main()
