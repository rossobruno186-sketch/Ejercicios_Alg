from ejercicio10 import Cola, arribar, atender, cola_vacia

def eliminar_por_posicion(cola, posicion):
    """
    Elimina el elemento en la posición dada (indexado desde 0).
    Mantiene el resto de la cola intacta.
    """
    cola_aux = Cola()
    pos_actual = 0
    elemento_eliminado = None

    # Desencolamos y filtramos
    while not cola_vacia(cola):
        item = atender(cola)
        if pos_actual == posicion:
            elemento_eliminado = item  # Lo encontramos, no lo guardamos
        else:
            arribar(cola_aux, item)
        pos_actual += 1

    # Restauramos la cola original
    while not cola_vacia(cola_aux):
        arribar(cola, atender(cola_aux))

    return elemento_eliminado

# --- Ejemplo de Uso / Pruebas ---
if __name__ == "__main__":
    mi_cola = Cola()
    for x in ['A', 'B', 'C', 'D', 'E']:
        arribar(mi_cola, x)
        
    print("Cola original (frente a final): A, B, C, D, E")
    pos = 2  # Debería eliminar 'C'
    eliminado = eliminar_por_posicion(mi_cola, pos)
    
    print(f"Elemento eliminado en la posición {pos}: {eliminado}")
    print("Cola resultante:")
    while not cola_vacia(mi_cola):
        print(atender(mi_cola), end=" ")