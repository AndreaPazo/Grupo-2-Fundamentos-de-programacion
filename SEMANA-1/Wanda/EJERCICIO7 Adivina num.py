# =========================================================
#EJERCICIO 07 - ADIVINA EL NÚMERO (Do-While / Repetir-Hasta)
#Estructura REPETITIVA "Repetir...Hasta Que"
#Se usara while True: ... if condicion: break
# =========================================================

#Necesita la librería random para generar el número secreto
import random

#Genera un número aleatorio entre 1 y 100 (el número secreto)
numero_secreto = random.randint(1, 100)

#Contador de intentos, empieza en 0
intentos = 0

print("Adivina el número secreto entre 1 y 100")

#Bucle "Repetir...Hasta Que adivine el número"
while True:

    #Pedir un intento al usuario
    intento = int(input("Ingresa tu número: "))
    intentos = intentos + 1  # sumamos 1 al contador de intentos

    #Compara el intento con el número secreto
    if intento < numero_secreto:
        print("El número secreto es MAYOR que tu intento.")

    elif intento > numero_secreto:
        print("El número secreto es MENOR que tu intento.")

    else:
        #Si no es ni mayor ni menor, entonces acertó
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # rompemos el bucle porque ya terminó el juego