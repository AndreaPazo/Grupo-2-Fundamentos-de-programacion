

# Lee estudiantes.csv con el módulo csv. Calcula promedio por
# alumno, muestra el top alumno y cuántos aprobaron (prom ≥ 13).
# Tip: usa csv.DictReader y max() con lambda como key


import csv
from pathlib import Path #llamamos a la libreria path para poder usarla en la ruta del archivo csv

# ruta_csv = Path(__file__).parent / "estudiantes.csv"
ruta_csv = Path(__file__).parent / "estudiantes.csv"

alumnos = []

# 1. Leer el archivo CSV
with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)

  for fila in lector:
    nombre = fila["nombre"]
    # Toma todas las columnas de notas (todas menos "nombre") y las convierte a número
    notas = [float(valor) for clave, valor in fila.items() if clave != "nombre"]
    promedio = sum(notas) / len(notas)

    alumnos.append({"nombre": nombre, "promedio": promedio})

# 2. Mostrar promedio por alumno
print("--- Promedio por alumno ---")
for alumno in alumnos:
  print(f"{alumno['nombre']}: {alumno['promedio']:.2f}")

# 3. Mostrar el top alumno usando max() con lambda como key
top_alumno = max(alumnos, key=lambda x: x["promedio"])
print(
    f"\nTop alumno: {top_alumno['nombre']} ({top_alumno['promedio']:.2f})"
)

# 4. Contar cuántos aprobaron (promedio >= 13)
aprobados = sum(1 for alumno in alumnos if alumno["promedio"] >= 13)
print(f"Aprobados (prom >= 13): {aprobados}")