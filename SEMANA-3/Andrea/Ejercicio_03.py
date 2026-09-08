# Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio, la nota
# mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno que muestre
# un reporte formateado

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minimo = min(notas)
    maximo = max(notas)

    return promedio, minimo, maximo

def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)

    print("----- REPORTE DE NOTAS -----")
    print(f"Alumno: {nombre}")
    print(f"Notas: {notas}")
    print(f"Promedio: {prom:.1f}")
    print(f"Nota mínima: {mn}")
    print(f"Nota máxima: {mx}")


nombre = input("Ingrese el nombre del alumno: ")
notas = [15, 18, 12, 15, 19]

mostrar_resultado(nombre, notas)