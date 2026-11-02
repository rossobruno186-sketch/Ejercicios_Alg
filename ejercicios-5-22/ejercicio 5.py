# 5. Desarrollar una función que permita convertir un número romano en un número decimal 
def romano_a_decimal (romano):

    valores= {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C': 100,}

    total = 0
    valoranterior = 0
    for letra in reversed (romano):
        valoractual = valores [letra]
        if valoractual < valoranterior:
            total -= valoractual
        else:
            total += valoractual
            valoranterior = valoractual
    return total
entrada = input("Escribí un número romano (ej: XIV): ")
resultado = romano_a_decimal(entrada)
print(f"El número decimal es: {resultado}")
        


