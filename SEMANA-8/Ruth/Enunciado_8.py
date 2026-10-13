

# Sistema de Calificaciones con Estructuras Combinadas
# Crea un sistema que maneje un diccionario de listas donde las claves son materias
# y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
# Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
# de cada materia y generar un reporte ordenado por promedio general de mayor a menor.


# 1. Definición de la lista de nombres y el diccionario de materias (arreglos paralelos)
nombres = ["Ana", "Carlos", "Beatriz", "David"]

materias_notas = {
    "Matemáticas": [16.5, 14.0, 19.0, 12.5],
    "Programación": [18.0, 15.5, 17.5, 16.0],
    "Física": [15.0, 13.5, 18.0, 14.0]
}


# 2. Función para calcular el promedio por materia
def calcular_promedio_materias(dict_materias):
    promedios = {}
    for materia, notas in dict_materias.items():
        if notas:
            promedios[materia] = sum(notas) / len(notas)
        else:
            promedios[materia] = 0.0
    return promedios


# 3. Función para encontrar al mejor estudiante de cada materia
def mejor_estudiante_por_materia(lista_nombres, dict_materias):
    mejores = {}
    for materia, notas in dict_materias.items():
        if notas:
            max_nota = max(notas)
            indice_max = notas.index(max_nota)
            mejor_alumno = lista_nombres[indice_max]
            mejores[materia] = {"estudiante": mejor_alumno, "nota": max_nota}
    return mejores


# 4. Función para generar un reporte ordenado por promedio general de mayor a menor
def reporte_general_ordenado(lista_nombres, dict_materias):
    reporte = []
    total_materias = len(dict_materias)
    
    # Recorremos cada estudiante según su índice en la lista paralela de nombres
    for i, nombre in enumerate(lista_nombres):
        suma_notas = 0
        for notas in dict_materias.values():
            suma_notas += notas[i]
            
        promedio_general = suma_notas / total_materias if total_materias > 0 else 0.0
        
        reporte.append({
            "nombre": nombre,
            "promedio_general": promedio_general
        })
        
    # Ordenar de mayor a menor según el promedio general
    reporte_ordenado = sorted(reporte, key=lambda x: x["promedio_general"], reverse=True)
    return reporte_ordenado


# --- Ejecución y pruebas del sistema ---

print("=" * 55)
print(f"{'SISTEMA DE CALIFICACIONES':^55}")
print("=" * 55)

# A) Promedio por materia
promedios_mat = calcular_promedio_materias(materias_notas)
print("\n PROMEDIO POR MATERIA:")
print("-" * 55)
for materia, prom in promedios_mat.items():
    print(f"  - {materia:<15} : {prom:.2f}")

# B) Mejor estudiante por materia
mejores_mat = mejor_estudiante_por_materia(nombres, materias_notas)
print("\n MEJOR ESTUDIANTE POR MATERIA:")
print("-" * 55)
for materia, info in mejores_mat.items():
    print(f"  - {materia:<15} : {info['estudiante']} (Nota: {info['nota']})")

# C) Reporte ordenado por promedio general de mayor a menor
ranking_general = reporte_general_ordenado(nombres, materias_notas)
print("\n RANKING GENERAL DE ESTUDIANTES (Promedio más alto a más bajo):")
print("-" * 55)
print(f"{'POSICIÓN':<10} | {'ESTUDIANTE':<15} | {'PROMEDIO GENERAL':<16}")
print("-" * 55)
for posicion, est in enumerate(ranking_general, start=1):
    print(f"{posicion}°          | {est['nombre']:<15} | {est['promedio_general']:<16.2f}")
print("=" * 55)