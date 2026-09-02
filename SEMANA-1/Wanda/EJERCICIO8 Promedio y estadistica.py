#=====================================================
#EJERCICIO 08 - PROMEDIO Y ESTADÍSTICAS DE NOTAS
#Estructura Repetitiva "Para" (for) + CONDICIONALES
#=======================================================

#Datos de entrada: n (cantidad de notas a ingresar)
n = int(input("¿Cuántas notas desea ingresar?: "))

#Variables donde guardaremos los resultados
suma_notas = 0        # para acumular la suma de todas las notas
nota_mas_alta = 0     # guardará la nota más alta encontrada
nota_mas_baja = 20    # empezamos con el máximo posible (20) para que la primera nota sea menor
aprobados = 0          # contador de estudiantes que aprobaron (nota >= 11)

#Por cada nota, una por una, usando un bucle "Para"
for i in range(1, n + 1):
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))

    #Sumando cada nota para luego calcular el promedio
    suma_notas = suma_notas + nota

    #Compara si esta nota es la más alta hasta ahora
    if nota > nota_mas_alta:
        nota_mas_alta = nota

    #Compara si esta nota es la más baja hasta ahora
    if nota < nota_mas_baja:
        nota_mas_baja = nota

    #Si la nota es mayor o igual a 11, el estudiante aprobó
    if nota >= 11:
        aprobados = aprobados + 1

#Calculamos el promedio (fuera del bucle, cuando ya terminamos de leer todo)
promedio = suma_notas / n

#Mostrar las estadísticas completas
print("----------------------------------------")
print("ESTADÍSTICAS")
print("----------------------------------------")
print(f"Promedio general:      {promedio:.2f}")
print(f"Nota más alta:         {nota_mas_alta}")
print(f"Nota más baja:         {nota_mas_baja}")
print(f"Estudiantes aprobados: {aprobados} de {n}")