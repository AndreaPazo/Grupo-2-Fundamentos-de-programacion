

#Solicita N notas al usuario. Calcula el promedio, la nota más alta, la más baja y cuántos estudiantes
#aprobaron (nota >= 11). Muestra estadísticas completas.

# Solicitar el número de notas al usuario
# Solicitar el número de notas al usuario
num_notas = int(input("Ingrese el número de notas: "))

# Variables para acumular y calcular estadísticas
suma_notas = 0
aprobados = 0
nota_maxima = None
nota_minima = None

for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    
    # Acumular la suma total de notas
    suma_notas += nota
    
    # Contar aprobados
    if nota >= 11:
        aprobados += 1
        
    # Inicializar o actualizar la nota máxima
    if nota_maxima is None or nota > nota_maxima:
        nota_maxima = nota
        
    # Inicializar o actualizar la nota mínima
    if nota_minima is None or nota < nota_minima:
        nota_minima = nota

# Verificar que se hayan ingresado notas para evitar división por cero
if num_notas > 0:
    promedio = suma_notas / num_notas

    print(f"\n--- Estadísticas Completa ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    print(f"Estudiantes aprobados: {aprobados}")
else:
    print("No se ingresaron notas para calcular estadísticas.")