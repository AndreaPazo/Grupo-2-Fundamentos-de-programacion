
# Lista de Diccionario de Estudiantes
# Crea una lista de diccionarios para 4 estudiantes con los campos: 'nombre', 'carrera' y 'promedio'.
# Imprime el nombre y promedio de cada estudiante.
# Luego muestra el nombre del estudiante con el promedio más alto.


# 1. Creación de la lista de diccionarios para 4 estudiantes
estudiantes = [
    {"nombre": "Ruth", "carrera": "Derecho", "promedio": 18.5},
    {"nombre": "Carlos", "carrera": "Contabilidad", "promedio": 16.0},
    {"nombre": "Andrea", "carrera": "Ingeniería", "promedio": 19.2},
    {"nombre": "Luis", "carrera": "Medicina", "promedio": 15.8}
]

# 2. Imprimir el nombre y promedio de cada estudiante
print("=" * 45)
print(f"{'REPORTE DE ESTUDIANTES':^45}")
print("=" * 45)
print(f"{'NOMBRE':<15} | {'CARRERA':<22} | {'PROMEDIO':<8}")
print("-" * 45)

for est in estudiantes:
    print(f"{est['nombre']:<15} | {est['carrera']:<22} | {est['promedio']:<8}")

print("-" * 45)

# 3. Mostrar el nombre del estudiante con el promedio más alto
# La función max() busca el valor máximo evaluando la clave 'promedio' de cada diccionario
estudiante_top = max(estudiantes, key=lambda x: x['promedio'])

print(f"Estudiante con el promedio más alto: {estudiante_top['nombre']} (Promedio: {estudiante_top['promedio']})")
print("=" * 45)