#===============================================
#EJERCICIO 03 - TABLA DE MULTIPLICAR
#Estructura Repetitiva 
#==================================================
#Datos
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
 
#range(1, 11) genera los números del 1 al 10
#(el 11 no se incluye, por eso ponemos uno más del límite que queremos)
print(f"--- Tabla del {numero} ---")
 
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
 
