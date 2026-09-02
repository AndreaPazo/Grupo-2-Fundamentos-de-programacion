import random  # librería para generar números aleatorios

numero_secreto = random.randint(1, 100)  # número aleatorio entre 1 y 100 (incluye ambos)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-100): "))
    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es MAYOR")
    elif intento > numero_secreto:
        print("El número secreto es MENOR")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        break  # termina el bucle porque ya acertó