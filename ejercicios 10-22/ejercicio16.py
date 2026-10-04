from Heap import Heap  
naves = [
    {"nombre": "Halcón Milenario", "largo": 34.75, "tripulacion": 4, "pasajeros": 6},
    {"nombre": "Estrella de la Muerte", "largo": 120000.0, "tripulacion": 342953, "pasajeros": 843342},
    {"nombre": "AT-AT", "largo": 20.0, "tripulacion": 3, "pasajeros": 40},
    {"nombre": "X-Wing", "largo": 12.5, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "TIE Fighter", "largo": 9.2, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "Star Destroyer", "largo": 1600.0, "tripulacion": 37000, "pasajeros": 38000},
    {"nombre": "AT-ST", "largo": 9.0, "tripulacion": 2, "pasajeros": 0},
]

naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['largo']))
print("A. Naves ordenadas por nombre (ascendente) y largo (descendente):")
for n in naves_ordenadas:
    print(f"   - {n['nombre']} (Largo: {n['largo']})")

print("\nB. Información específica:")
for n in naves:
    if n['nombre'] in ["Halcón Milenario", "Estrella de la Muerte"]:
        print(f"   - {n}")

print("\nC. Top 5 naves con más pasajeros:")
heap_pasajeros = Heap()
for n in naves:
    heap_pasajeros.add_element([n['pasajeros'], n['nombre']])

for i in range(min(5, heap_pasajeros.size())):
    max_pasajeros = heap_pasajeros.delete_element()
    print(f"   {i+1}. {max_pasajeros[1]} con {max_pasajeros[0]} pasajeros")

print("\nD. Nave con mayor tripulación:")
heap_tripulacion = Heap()
for n in naves:
    heap_tripulacion.add_element([n['tripulacion'], n['nombre']])

nave_max_trip = heap_tripulacion.delete_element()
print(f"   - {nave_max_trip[1]} requiere {nave_max_trip[0]} tripulantes.")

print("\nE. Naves que comienzan con 'AT':")
for n in naves:
    if n['nombre'].startswith("AT"):
        print(f"   - {n['nombre']}")

print("\nF. Naves con 6 o más pasajeros:")
for n in naves:
    if n['pasajeros'] >= 6:
        print(f"   - {n['nombre']} (Pasajeros: {n['pasajeros']})")

print("\nG. Nave más pequeña y más grande:")
nave_mas_pequena = min(naves, key=lambda x: x['largo'])
nave_mas_grande = max(naves, key=lambda x: x['largo'])
print(f"   - Más pequeña: {nave_mas_pequena}")
print(f"   - Más grande: {nave_mas_grande}")