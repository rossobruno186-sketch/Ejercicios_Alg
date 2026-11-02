from tree import BinaryTree
from datos import lista_100_pokemons 

class PokemonTree(BinaryTree):
    
    def search_by_proximity(self, prefix):
        results = []
        def __search(root, prefix):
            if root is not None:
                if prefix.lower() in root.value.lower():
                    results.append(root.other_values)
                __search(root.left, prefix)
                __search(root.right, prefix)
        __search(self.root, prefix)
        return results

    def get_by_types(self, types_list):
        results = []
        def __search(root):
            if root is not None:
                if root.value in types_list:
                    results.append(root.other_values['name'])
                __search(root.left)
                __search(root.right)
        __search(self.root)
        return list(set(results))

    def count_types(self):
        type_count = {}
        def __count(root):
            if root is not None:
                type_count[root.value] = type_count.get(root.value, 0) + 1
                __count(root.left)
                __count(root.right)
        __count(self.root)
        return type_count

    def count_feature(self, feature_key):
        count = [0]
        def __count(root):
            if root is not None:
                if root.other_values.get(feature_key, False):
                    count[0] += 1
                __count(root.left)
                __count(root.right)
        __count(self.root)
        return count[0]
    
    def get_weak_to(self, weaknesses):
        results = []
        def __search(root):
            if root is not None:
                if any(w in root.other_values['weaknesses'] for w in weaknesses):
                    results.append(root.other_values['name'])
                __search(root.left)
                __search(root.right)
        __search(self.root)
        return list(set(results))

    def show_specific_weaknesses(self):
        def __search(root):
            if root is not None:
                debilidades = root.other_values['weaknesses']
                rivales = []
                if 'eléctrico' in debilidades:
                    rivales.append('Jolteon')
                if 'roca' in debilidades:
                    rivales.append('Lycanroc y Tyrantrum') 
                elif 'dragón' in debilidades:
                    rivales.append('Tyrantrum')

                if rivales:
                    print(f"{root.other_values['name']} es débil frente a: {', '.join(rivales)}")
                
                __search(root.left)
                __search(root.right)
        __search(self.root)

tree_name = PokemonTree()     
tree_number = PokemonTree()   
tree_type = PokemonTree()     

for poke_data in lista_100_pokemons:
    tree_name.insert_node(poke_data['name'], poke_data)
    tree_number.insert_node(poke_data['number'], poke_data)
    for t in poke_data['types']:
        tree_type.insert_node(t, poke_data)

print("=== EJERCICIO 1: GESTIÓN DE POKÉMONS CON ÁRBOLES ===\n")

print("--- 1. BÚSQUEDA INTERACTIVA ---")
num_input = input("Ingrese el número del Pokémon a buscar: ")
try:
    num_buscado = int(num_input)
    poke_num = tree_number.search(num_buscado)
    if poke_num:
        print(f"Resultado por número: {poke_num.other_values}")
    else:
        print("No se encontró ningún Pokémon con ese número.")
except ValueError:
    print("Entrada inválida. Debe ingresar un número entero.")

print("\n--- 2. BÚSQUEDA POR PROXIMIDAD DE NOMBRE ---")
nombre_input = input("Ingrese el nombre o parte del nombre del Pokémon a buscar: ")
prox_results = tree_name.search_by_proximity(nombre_input)
if prox_results:
    for p in prox_results:
        print(f"Encontrado: {p['name']} -> Datos: {p}")
else:
    print("No se encontraron coincidencias para el término ingresado.")


print("\n--- 3. POKÉMONS DE TIPO FANTASMA, FUEGO, ACERO Y ELÉCTRICO ---")
tipos_buscados = ['fantasma', 'fuego', 'acero', 'eléctrico']
pokemons_por_tipo = tree_type.get_by_types(tipos_buscados)
print(pokemons_por_tipo)

print("\n--- 4. LISTADO EN ORDEN ASCENDENTE POR NÚMERO ---")
tree_number.inorden()

print("\n--- 4. LISTADO EN ORDEN ASCENDENTE POR NOMBRE ---")
tree_name.inorden()

print("\n--- 4. LISTADO POR NIVEL (POR NOMBRE) ---")
tree_name.by_level()

print("\n--- 5. POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM ---")
tree_name.show_specific_weaknesses()

print("\n--- 6. CANTIDAD DE POKÉMONS POR TIPO ---")
print(tree_type.count_types())

print("\n--- 7 y 8. CANTIDAD CON MEGAEVOLUCIÓN Y GIGAMAX ---")
print(f"Cantidad con Megaevolución: {tree_name.count_feature('mega')}")
print(f"Cantidad con Forma Gigamax: {tree_name.count_feature('gigamax')}")
