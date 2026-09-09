
#Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio, la nota
#mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno que muestre
#un reporte formateado.

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    nota_minima = min(notas)
    nota_maxima = max(notas)
    return promedio, nota_minima, nota_maxima


def mostrar_resultado(nombre, notas):
    promedio, nota_minima, nota_maxima = calcular_promedio(notas)

    #salto de línea, centrar el texto y mostrar el reporte de notas
    print("\n--- Reporte de Notas ---")
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota mínima: {nota_minima}")
    print(f"Nota máxima: {nota_maxima}")

# Ejemplo de uso
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
notas_estudiante = [float(input(f"Ingrese la nota {i+1}: ")) for i in range(5)]
mostrar_resultado(nombre_estudiante, notas_estudiante)

