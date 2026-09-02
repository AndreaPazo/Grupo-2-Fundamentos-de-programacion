#=================================================
#EJERCICIO 06 - NÚMEROS PRIMOS HASTA N
#Estructura Repetitiva anidada (un "for" dentro de otro "for")
#Un número es PRIMO si solo se puede dividir exactamente entre 1 y ese mismo
#==============================================

#Para raíz cuadrada se importa la librería math
import math

#Datos
n = int(input("Ingrese el número N (mostraremos los primos desde 2 hasta N): "))

print(f"--- Números primos entre 2 y {n} ---")

#Recorre cada número desde 2 hasta N
for numero in range(2, n + 1):

    es_primo = True  # Suponemos que el número SÍ es primo, hasta que se demuestre lo contrario

    #Calcula la raíz cuadrada
    
    raiz = int(math.sqrt(numero))

    #si "numero" se puede dividir exactamente entre 2, 3, 4... hasta su raíz
    for divisor in range(2, raiz + 1):
        if numero % divisor == 0:
            # Si el resto es 0, entonces SÍ tiene un divisor -> no es primo
            es_primo = False
            break  # ya no necesitamos seguir revisando, salimos del bucle interno

    #Resultado 
    if es_primo:
        print(numero)