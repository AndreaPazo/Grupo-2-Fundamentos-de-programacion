# Analizador de notas CSV
# Lee estudiantes.csv con el módulo csv. Calcula promedio por alumno, muestra el top alumno y cuántos aprobaron (prom ≥ 13).

import csv

estudiantes = []

# Leer el archivo CSV
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        promedio = (float(fila["nota1"]) + float(fila["nota2"]) + float(fila["nota3"])) / 3

        estudiantes.append({
            "nombre": fila["nombre"],
            "promedio": promedio
        })

# Mostrar promedio por alumno
for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.2f}")

# Encontrar al alumno con mayor promedio
top = max(estudiantes, key=lambda x: x["promedio"])

print(f"\nMejor alumno: {top['nombre']} con {top['promedio']:.2f}")

# Contar alumnos aprobados
aprobados = sum(1 for estudiante in estudiantes if estudiante["promedio"] >= 13)

print(f"Cantidad de aprobados: {aprobados}")