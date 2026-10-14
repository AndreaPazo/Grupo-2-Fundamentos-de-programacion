# Lista de Diccionario de Estudiantes
# Crea una lista de diccionarios para 4 estudiantes con los campos: 
# 'nombre', 'carrera' y 'promedio'.
# Imprime el nombre y promedio de cada estudiante.
# Luego muestra el nombre del estudiante con el promedio más alto


# Lista de diccionarios de estudiantes
estudiantes = [
    {'nombre': 'Carlos', 'carrera': 'Ingeniería de Sistemas', 'promedio': 16.5},
    {'nombre': 'Ana', 'carrera': 'Administración', 'promedio': 18.2},
    {'nombre': 'Luis', 'carrera': 'Contabilidad', 'promedio': 15.8},
    {'nombre': 'María', 'carrera': 'Ingeniería Industrial', 'promedio': 17.4}
]

# 1. Imprimir el nombre y promedio de cada estudiante
print("LISTA DE ESTUDIANTES")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']} | Promedio: {estudiante['promedio']}")

# 2. Mostrar el estudiante con el promedio más alto
mejor_estudiante = max(estudiantes, key=lambda estudiante: estudiante['promedio'])

print("\nESTUDIANTE CON EL PROMEDIO MÁS ALTO")
print(f"Nombre: {mejor_estudiante['nombre']}")
print(f"Promedio: {mejor_estudiante['promedio']}")
