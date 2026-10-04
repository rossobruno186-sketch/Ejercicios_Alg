class NodoMCU:
    def __init__(self, nombre, is_hero):
        self.nombre = nombre
        self.is_hero = is_hero  # True: Héroe, False: Villano
        self.izq = None
        self.der = None

class ArbolMCU:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, is_hero):
        if self.raiz is None:
            self.raiz = NodoMCU(nombre, is_hero)
        else:
            self._insertar_recursivo(self.raiz, nombre, is_hero)

    def _insertar_recursivo(self, nodo, nombre, is_hero):
        if nombre < nodo.nombre:
            if nodo.izq is None:
                nodo.izq = NodoMCU(nombre, is_hero)
            else:
                self._insertar_recursivo(nodo.izq, nombre, is_hero)
        else:
            if nodo.der is None:
                nodo.der = NodoMCU(nombre, is_hero)
            else:
                self._insertar_recursivo(nodo.der, nombre, is_hero)

    def listar_villanos(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is not None:
            self.listar_villanos(nodo.izq, False)
            if not nodo.is_hero:
                print(f" - {nodo.nombre}")
            self.listar_villanos(nodo.der, False)

    def listar_heroes_con_c(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is not None:
            self.listar_heroes_con_c(nodo.izq, False)
            if nodo.is_hero and nodo.nombre.startswith('C'):
                print(f" - {nodo.nombre}")
            self.listar_heroes_con_c(nodo.der, False)

    def contar_heroes(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is None: return 0
        conteo = 1 if nodo.is_hero else 0
        return conteo + self.contar_heroes(nodo.izq, False) + self.contar_heroes(nodo.der, False)

    def buscar_y_modificar_proximidad(self, nodo, busqueda, nuevo_nombre):
        if nodo is not None:
            self.buscar_y_modificar_proximidad(nodo.izq, busqueda, nuevo_nombre)
            if busqueda.lower() in nodo.nombre.lower():
                print(f"Modificando '{nodo.nombre}' a '{nuevo_nombre}'")
                nodo.nombre = nuevo_nombre # Si cambia alfabéticamente drástico, se debería rearmar el árbol.
            self.buscar_y_modificar_proximidad(nodo.der, busqueda, nuevo_nombre)

    def listar_heroes_desc(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is not None:
            self.listar_heroes_desc(nodo.der, False)
            if nodo.is_hero:
                print(f" - {nodo.nombre}")
            self.listar_heroes_desc(nodo.izq, False)

    def generar_bosque(self, nodo, arbol_heroes, arbol_villanos):
        if nodo is not None:
            if nodo.is_hero:
                arbol_heroes.insertar(nodo.nombre, True)
            else:
                arbol_villanos.insertar(nodo.nombre, False)
            self.generar_bosque(nodo.izq, arbol_heroes, arbol_villanos)
            self.generar_bosque(nodo.der, arbol_heroes, arbol_villanos)

    def contar_nodos(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is None: return 0
        return 1 + self.contar_nodos(nodo.izq, False) + self.contar_nodos(nodo.der, False)


if __name__ == "__main__":
    arbol = ArbolMCU()
    
    datos = [
        ("Iron Man", True), ("Thanos", False), ("Captain America", True),
        ("Loki", False), ("Thor", True), ("Red Skull", False),
        ("Captain Marvel", True), ("Dr. Strang", True), ("Hela", False) # Error intencional
    ]
    for nombre, is_hero in datos:
        arbol.insertar(nombre, is_hero)

    print("--- B. Villanos (Alfabético) ---")
    arbol.listar_villanos()

    print("\n--- C. Superhéroes que empiezan con 'C' ---")
    arbol.listar_heroes_con_c()

    print(f"\n--- D. Cantidad total de Superhéroes: {arbol.contar_heroes()} ---")

    print("\n--- E. Modificando Doctor Strange (Búsqueda por proximidad) ---")
    arbol.buscar_y_modificar_proximidad(arbol.raiz, "Strang", "Doctor Strange")

    print("\n--- F. Superhéroes (Descendente) ---")
    arbol.listar_heroes_desc()

    print("\n--- G. Generando Bosque ---")
    arbol_heroes = ArbolMCU()
    arbol_villanos = ArbolMCU()
    arbol.generar_bosque(arbol.raiz, arbol_heroes, arbol_villanos)

    print(f"Nodos en Árbol Héroes: {arbol_heroes.contar_nodos()}")
    print(f"Nodos en Árbol Villanos: {arbol_villanos.contar_nodos()}")
    
    print("\nBarrido Alfabético Héroes:")
    arbol_heroes.listar_heroes_desc(inicial=True) # Usamos desc o crear una normal