# Promedio y Estadísticas
# Solicita N notas al usuario. Calcula el promedio, la nota más alta, la más baja y cuántos estudiantes
# aprobaron (nota >= 11). Muestra estadísticas completas

notas = int(input("Ingrese la cantidad de notas: "))

suma = 0
aprobados = 0
nota_mayor = None
nota_menor = None

for i in range(notas):
    while True:
        nota = float(input(f"Ingrese la nota {i + 1} (0-20): "))
        if nota >= 0 and nota <= 20:
            break
        print("La nota debe estar entre 0 y 20.")

    suma += nota

    if nota >= 11:
        aprobados += 1

    if nota_mayor is None or nota > nota_mayor:
        nota_mayor = nota

    if nota_menor is None or nota < nota_menor:
        nota_menor = nota

if notas > 0:
    promedio = suma / notas

    print("\n--- ESTADÍSTICAS COMPLETAS ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {nota_mayor}")
    print(f"Nota más baja: {nota_menor}")
    print(f"Estudiantes aprobados: {aprobados}")
else:
    print("No se ingresaron notas.")