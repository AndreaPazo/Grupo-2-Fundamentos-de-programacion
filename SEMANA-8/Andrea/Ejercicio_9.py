# Buscador Inteligente con Regex y Ordenamiento
# Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
# con campos 'titulo', 'autor' y 'año'. La función debe:
# 1) Buscar el query en título y autor (regex, case-insensitive).
# 2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
# 3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año.


import re

# Catálogo de libros
catalogo = [
    {'titulo': 'Python desde cero', 'autor': 'Ana García', 'año': 2022},
    {'titulo': 'Programación avanzada', 'autor': 'Luis Pérez', 'año': 2020},
    {'titulo': 'Python para principiantes', 'autor': 'Carlos Ruiz', 'año': 2024},
    {'titulo': 'Bases de datos', 'autor': 'Ana Torres', 'año': 2021},
    {'titulo': 'Introducción a Python', 'autor': 'Luis Python', 'año': 2019}
]

def buscador(catalogo, query):
    resultados = []

    for libro in catalogo:
        puntaje = 0

        # 1. Buscar el query en título y autor
        if re.search(query, libro['titulo'], re.IGNORECASE):
            puntaje += 2

        if re.search(query, libro['autor'], re.IGNORECASE):
            puntaje += 1

        # Guardar solo los libros que coinciden
        if puntaje > 0:
            resultados.append({
                'titulo': libro['titulo'],
                'autor': libro['autor'],
                'año': libro['año'],
                'puntaje': puntaje
            })

    # 2 y 3. Ordenar por puntaje descendente y luego por año ascendente
    resultados.sort(key=lambda libro: (-libro['puntaje'], libro['año']))

    return resultados


# Buscar libros
query = input("Ingrese el término de búsqueda: ")

resultados = buscador(catalogo, query)

# Mostrar resultados
print("\nRESULTADOS DE LA BÚSQUEDA")

for libro in resultados:
    print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Año: {libro['año']} | Puntaje: {libro['puntaje']}")
