def usar_la_fuerza(mochila, indice=0):
    """
    Busca de forma recursiva un 'sable de luz' en una mochila.
    """
    if indice >= len(mochila):
        print("Se han revisado todos los objetos y no hay rastro del sable de luz.")
        return False, indice

    objeto_actual = mochila[indice]
    print(f"Sacando objeto {indice + 1}: {objeto_actual}")

    if objeto_actual == "sable de luz":
        print(f"¡Que la fuerza te acompañe! Has encontrado tu sable de luz.")
        return True, indice + 1

    return usar_la_fuerza(mochila, indice + 1)

mochila_de_luke = ["comida", "holocron", "capa", "sable de luz", "brújula"]

encontrado, cantidad = usar_la_fuerza(mochila_de_luke)

if encontrado:
    print(f"\nResultado: Se encontró el sable tras sacar {cantidad} objetos.")
else:
    print(f"\nResultado: El sable no estaba en la mochila.")