# Adivina el Número (Do-While)
# Genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. 
# En cada intento, indica si el número secreto es mayor o menor. Cuenta los intentos.

import random

numero=random.randint(1,100)
intentos=0  

while True:
    adivinanza=int(input("Adivina el numero secreto entre (1,100): "))
    intentos+=1
    if adivinanza<numero:
        print("El numero secreto es mayor")
    elif adivinanza>numero:
        print("El numero secreto es menor")
    else:
        print(f"Felicidades! Adivinaste el numero secreto: {numero}, en {intentos} intentos.")
        break