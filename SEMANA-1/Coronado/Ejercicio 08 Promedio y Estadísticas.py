n = int(input("¿Cuántas notas vas a ingresar?: "))

notas = []  # lista vacía donde se guardarán las notas

for i in range(n):
    nota = float(input(f"Ingresa la nota {i + 1}: "))
    notas.append(nota)  # agrega la nota a la lista

promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)
aprobados = 0

for nota in notas: # notas aprobados de 11 o más.
    if nota >= 11:
        aprobados += 1  

print("--- Estadísticas ---")
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print(f"Estudiantes aprobados: {aprobados} de {len(notas)}")