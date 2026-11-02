from collections import deque

class NodoCriatura:
    def __init__(self, nombre, derrotado_por):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""      # b. Breve descripción
        self.capturada = None      # g. Quién la capturó
        self.izq = None
        self.der = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por):
        if self.raiz is None:
            self.raiz = NodoCriatura(nombre, derrotado_por)
        else:
            self._insertar_recursivo(self.raiz, nombre, derrotado_por)

    def _insertar_recursivo(self, nodo, nombre, derrotado_por):
        if nombre < nodo.nombre:
            if nodo.izq is None:
                nodo.izq = NodoCriatura(nombre, derrotado_por)
            else:
                self._insertar_recursivo(nodo.izq, nombre, derrotado_por)
        elif nombre > nodo.nombre:
            if nodo.der is None:
                nodo.der = NodoCriatura(nombre, derrotado_por)
            else:
                self._insertar_recursivo(nodo.der, nombre, derrotado_por)

    def inorden(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is not None:
            self.inorden(nodo.izq, False)
            print(f"Criatura: {nodo.nombre} | Derrotada por: {nodo.derrotado_por}")
            self.inorden(nodo.der, False)

    def buscar_nodo(self, nodo, busqueda, exacta=True):
        if nodo is None: return None
        if exacta:
            if nodo.nombre == busqueda: return nodo
            elif busqueda < nodo.nombre: return self.buscar_nodo(nodo.izq, busqueda, exacta)
            else: return self.buscar_nodo(nodo.der, busqueda, exacta)
        else:
            resultados = []
            if busqueda.lower() in nodo.nombre.lower():
                resultados.append(nodo)
            if nodo.izq: resultados.extend(self.buscar_nodo(nodo.izq, busqueda, exacta))
            if nodo.der: resultados.extend(self.buscar_nodo(nodo.der, busqueda, exacta))
            return resultados

    def recolectar_derrotas(self, nodo, conteo):
        if nodo is not None:
            if nodo.derrotado_por and nodo.derrotado_por != "-":
                conteo[nodo.derrotado_por] = conteo.get(nodo.derrotado_por, 0) + 1
            self.recolectar_derrotas(nodo.izq, conteo)
            self.recolectar_derrotas(nodo.der, conteo)

    def top_3_heroes(self):
        conteo = {}
        self.recolectar_derrotas(self.raiz, conteo)
        ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
        return ordenados[:3]

    def listar_derrotadas_por(self, nodo, heroe):
        if nodo is not None:
            self.listar_derrotadas_por(nodo.izq, heroe)
            if nodo.derrotado_por == heroe:
                print(f" - {nodo.nombre}")
            self.listar_derrotadas_por(nodo.der, heroe)

    def listar_no_derrotadas(self, nodo=None, inicial=True):
        if inicial: nodo = self.raiz
        if nodo is not None:
            self.listar_no_derrotadas(nodo.izq, False)
            if nodo.derrotado_por == "-":
                print(f" - {nodo.nombre}")
            self.listar_no_derrotadas(nodo.der, False)

    def listar_capturadas_por(self, nodo, heroe):
        if nodo is not None:
            self.listar_capturadas_por(nodo.izq, heroe)
            if nodo.capturada == heroe:
                print(f" - {nodo.nombre}")
            self.listar_capturadas_por(nodo.der, heroe)

    def listado_por_niveles(self):
        if not self.raiz: return
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            print(f" - {nodo.nombre}")
            if nodo.izq: cola.append(nodo.izq)
            if nodo.der: cola.append(nodo.der)

    def eliminar(self, raiz, clave):
        if raiz is None: return raiz
        if clave < raiz.nombre:
            raiz.izq = self.eliminar(raiz.izq, clave)
        elif clave > raiz.nombre:
            raiz.der = self.eliminar(raiz.der, clave)
        else:
            if raiz.izq is None: return raiz.der
            elif raiz.der is None: return raiz.izq
            
            temp = self._min_valor_nodo(raiz.der)
            raiz.nombre = temp.nombre
            raiz.derrotado_por = temp.derrotado_por
            raiz.der = self.eliminar(raiz.der, temp.nombre)
        return raiz

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

if __name__ == "__main__":
    arbol = ArbolCriaturas()
    
    datos = [
        ("Ceto", "-"), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
        ("Dino", "-"), ("Pefredo", "-"), ("Enio", "-"), ("Escila", "-"),
        ("Caribdis", "-"), ("Euríale", "-"), ("Esteno", "-"),
        ("Medusa", "Perseo"), ("Ladón", "Heracles"), ("Águila del Cáucaso", "-"),
        ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
        ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"),
        ("Dragón de la Cólquida", "-"), ("Cerbero", "-"),
        ("Cerda de Cromión", "Teseo"), ("Ortro", "Heracles"),
        ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"),
        ("Gerión", "Heracles"), ("Cloto", "-"), ("Láquesis", "-"),
        ("Átropos", "-"), ("Minotauro de Creta", "Teseo"),
        ("Harpías", "-"), ("Argos Panoptes", "Hermes"),
        ("Aves del Estínfalo", "-"), ("Talos", "Medea"),
        ("Sirenas", "-"), ("Pitón", "Apolo"), ("Cierva de Cerinea", "-"),
        ("Basilisco", "-"), ("Jabalí de Erimanto", "-")
    ]
    
    for c, d in datos:
        arbol.insertar(c, d)

    print("--- A. Listado Inorden ---")
    arbol.inorden()

    print("\n--- C. Info de Talos ---")
    talos = arbol.buscar_nodo(arbol.raiz, "Talos")
    if talos: print(f"Nombre: {talos.nombre}, Derrotado por: {talos.derrotado_por}")

    print("\n--- D. Top 3 Héroes que más derrotaron ---")
    top3 = arbol.top_3_heroes()
    for heroe, cantidad in top3:
        print(f"{heroe}: {cantidad} criaturas")

    print("\n--- E. Criaturas derrotadas por Heracles ---")
    arbol.listar_derrotadas_por(arbol.raiz, "Heracles")

    print("\n--- F. Criaturas no derrotadas ---")
    arbol.listar_no_derrotadas()

    print("\n--- H. Marcando capturadas por Heracles ---")
    para_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for c in para_capturar:
        nodo = arbol.buscar_nodo(arbol.raiz, c)
        if nodo: nodo.capturada = "Heracles"

    print("\n--- I. Búsqueda por coincidencia ('Creta') ---")
    coincidencias = arbol.buscar_nodo(arbol.raiz, "Creta", exacta=False)
    for c in coincidencias: print(f" - {c.nombre}")

    print("\n--- J. Eliminando Basilisco y Sirenas ---")
    arbol.raiz = arbol.eliminar(arbol.raiz, "Basilisco")
    arbol.raiz = arbol.eliminar(arbol.raiz, "Sirenas")

    print("\n--- K. Modificando Aves del Estínfalo ---")
    aves = arbol.buscar_nodo(arbol.raiz, "Aves del Estínfalo")
    if aves:
        aves.derrotado_por = "Heracles (derrotó a varias)"

    print("\n--- L. Modificando 'Ladón' a 'Dragón Ladón' ---")
    ladon = arbol.buscar_nodo(arbol.raiz, "Ladón")
    if ladon:
        derrotador = ladon.derrotado_por
        arbol.raiz = arbol.eliminar(arbol.raiz, "Ladón")
        arbol.insertar("Dragón Ladón", derrotador)

    print("\n--- M. Listado por nivel ---")
    arbol.listado_por_niveles()

    print("\n--- N. Criaturas capturadas por Heracles ---")
    arbol.listar_capturadas_por(arbol.raiz, "Heracles")