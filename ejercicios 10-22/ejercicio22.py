class NodoCola:
    def __init__(self, info=None):
        self.info = info
        self.sig = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

def cola_vacia(cola):
    return cola.frente is None

def arribar(cola, elemento):
    nuevo_nodo = NodoCola(elemento)
    if cola_vacia(cola):
        cola.frente = nuevo_nodo
    else:
        cola.final.sig = nuevo_nodo
    cola.final = nuevo_nodo
    cola.tamanio += 1

def atender(cola):
    if cola_vacia(cola):
        return None
    aux = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return aux

def frente(cola):
    if cola_vacia(cola):
        return None
    return cola.frente.info

def tamanio(cola):
    return cola.tamanio