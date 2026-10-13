

# Buscador Inteligente con Regex y Ordenamiento
# Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
# con campos 'titulo', 'autor' y 'año'. La función debe:
# 1) Buscar el query en título y autor (regex, case-insensitive).
# 2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
# 3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año.


import re

catalogo = [
    {"titulo": "Python desde cero", "autor": "Ana García", "año": 2022},
    {"titulo": "Programación en Java", "autor": "Luis Pérez", "año": 2020},
    {"titulo": "Python avanzado", "autor": "Luis Pérez", "año": 2024},
    {"titulo": "Introducción a Python", "autor": "María López", "año": 2021},
    {"titulo": "Bases de datos", "autor": "Ana García", "año": 2023}
]

def buscador(catalogo, query):
    resultados = []
    patron = re.compile(re.escape(query), re.IGNORECASE)

    for libro in catalogo:
        puntaje = 0

        # Buscar coincidencias en el título
        if patron.search(libro["titulo"]):
            puntaje += 2

        # Buscar coincidencias en el autor
        if patron.search(libro["autor"]):
            puntaje += 1

        # Agregar solo los libros que coinciden
        if puntaje > 0:
            resultados.append({
                "titulo": libro["titulo"],
                "autor": libro["autor"],
                "año": libro["año"],
                "puntaje": puntaje
            })

    # Ordenar por puntaje descendente y año ascendente
    resultados.sort(key=lambda libro: (-libro["puntaje"], libro["año"]))

    return resultados


# Probar el buscador
query = input("Ingrese el título o autor que desea buscar: ")

encontrados = buscador(catalogo, query)

print("\nRESULTADOS DE BÚSQUEDA:")
print("-" * 60)
if encontrados:
    for libro in encontrados:
        print(f"- Título: {libro['titulo']}")
        print(f"  Autor:  {libro['autor']}")
        print(f"  Año:    {libro['año']}")
        print(f"  Puntaje: {libro['puntaje']}")
        print("-" * 60)
else:
    print("No se encontraron resultados.")