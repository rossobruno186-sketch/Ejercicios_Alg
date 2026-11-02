import random
import time

def busqueda_secuencial(lista, buscado):
   
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    return -1

def busqueda_binaria(lista, buscado):
   
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def ejecutar_pruebas():
    tamanos = [100000, 1000000, 10000000]
    
    for n in tamanos:
        print(f"\n{'-'*50}")
        print(f"Generando lista de {n:,} elementos... (puede tardar un momento)")
        
        lista = [random.randint(1, n) for _ in range(n)]
        
        buscado = -1 
        
        inicio_sec = time.perf_counter()
        busqueda_secuencial(lista, buscado)
        fin_sec = time.perf_counter()
        tiempo_sec = fin_sec - inicio_sec
        
        print(f"-> Tiempo Búsqueda Secuencial: {tiempo_sec:.6f} segundos")
        
        lista.sort()
        
        inicio_bin = time.perf_counter()
        busqueda_binaria(lista, buscado)
        fin_bin = time.perf_counter()
        tiempo_bin = fin_bin - inicio_bin
        
        print(f"-> Tiempo Búsqueda Binaria:    {tiempo_bin:.6f} segundos")

if __name__ == "__main__":
    ejecutar_pruebas()