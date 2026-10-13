

# Sistema de Calificaciones con Estructuras Combinadas
# Crea un sistema que maneje un diccionario de listas donde las claves son materias
# y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
# Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
# de cada materia y generar un reporte ordenado por promedio general de mayor a menor.



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

        if patron.search(libro["titulo"]):
            puntaje += 2

        if patron.search(libro["autor"]):
            puntaje += 1

        if puntaje > 0:
            resultados.append({
                "titulo": libro["titulo"],
                "autor": libro["autor"],
                "año": libro["año"],
                "puntaje": puntaje
            })

    resultados.sort(key=lambda libro: (-libro["puntaje"], libro["año"]))

    return resultados


# Buscar libros
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
