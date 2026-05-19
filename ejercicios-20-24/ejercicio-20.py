from stack import Stack

def registrar_movimiento(pila_movimientos, pasos, direccion):
    pila_movimientos.push({'pasos': pasos, 'direccion': direccion})
    print(f"Ida -> Pasos: {pasos}, Dirección: {direccion}")

def retornar_al_origen(pila_ida):
    direcciones_opuestas = {
        'norte': 'sur',
        'sur': 'norte',
        'este': 'oeste',
        'oeste': 'este',
        'noreste': 'suroeste',
        'suroeste': 'noreste',
        'noroeste': 'sureste',
        'sureste': 'noroeste'
    }
    
    print("\nIniciando secuencia de regreso...")

    while pila_ida.size() > 0:
        movimiento = pila_ida.pop()
        pasos = movimiento['pasos']
        direccion = movimiento['direccion']
        direccion_opuesta = direcciones_opuestas[direccion]
        
        print(f"Regreso -> Pasos: {pasos}, Dirección: {direccion_opuesta}")

if __name__ == "__main__":
    print("--- EJERCICIO 20: MOVIMIENTOS DEL ROBOT ---")
    
    pila_movimientos = Stack()

    
    registrar_movimiento(pila_movimientos, 10, 'norte')
    registrar_movimiento(pila_movimientos, 5, 'este')
    registrar_movimiento(pila_movimientos, 3, 'noreste')
    registrar_movimiento(pila_movimientos, 20, 'sur')
    
    retornar_al_origen(pila_movimientos)
