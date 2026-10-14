# Sistema de Calificaciones con Estructuras Combinadas
# Crea un sistema que maneje un diccionario de listas donde las claves son materias
# y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
# Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
# de cada materia y generar un reporte ordenado por promedio general de mayor a menor.


# Lista de nombres de estudiantes
nombres = ["Ana", "Luis", "Mía", "Carlos"]

# Diccionario de listas de notas por materia
materias = {
    "Matemática": [18, 15, 20, 14],
    "Comunicación": [16, 19, 17, 15],
    "Ciencia": [17, 14, 18, 20]
}

# 1. Función para calcular el promedio por materia
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# 2. Función para encontrar al mejor estudiante de cada materia
def mejor_estudiante(nombres, notas):
    mayor_nota = max(notas)
    posicion = notas.index(mayor_nota)
    return nombres[posicion], mayor_nota

# 3. Función para generar el reporte ordenado por promedio general
def generar_reporte(nombres, materias):
    reporte = []

    for i in range(len(nombres)):
        suma_notas = 0

        for notas in materias.values():
            suma_notas += notas[i]

        promedio_general = suma_notas / len(materias)

        reporte.append({
            "nombre": nombres[i],
            "promedio": promedio_general
        })

    reporte.sort(key=lambda estudiante: estudiante["promedio"], reverse=True)

    return reporte


# Mostrar el promedio de cada materia y su mejor estudiante
print("PROMEDIO Y MEJOR ESTUDIANTE POR MATERIA")

for materia, notas in materias.items():
    promedio = calcular_promedio(notas)
    nombre_mejor, nota_mejor = mejor_estudiante(nombres, notas)

    print(f"\nMateria: {materia}")
    print(f"Promedio de la materia: {promedio:.2f}")
    print(f"Mejor estudiante: {nombre_mejor} - Nota: {nota_mejor}")


# Mostrar el reporte general ordenado
print("\nREPORTE GENERAL DE ESTUDIANTES")

reporte = generar_reporte(nombres, materias)

for i, estudiante in enumerate(reporte, start=1):
    print(f"{i}°. {estudiante['nombre']} - Promedio general: {estudiante['promedio']:.2f}")
