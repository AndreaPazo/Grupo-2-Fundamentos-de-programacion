import math  # librería para usar la raíz cuadrada

n = int(input("Ingresa un número N: "))

print(f"Números primos entre 2 y {n}:")

for numero in range(2, n + 1):
    es_primo = True
    limite = int(math.sqrt(numero))  # raíz cuadrada del número, redondeada hacia abajo

    for divisor in range(2, limite + 1):
        if numero % divisor == 0:
            es_primo = False
            break  # corta el bucle apenas encuentra un divisor, ya no es primo

    if es_primo:
        print(numero, end=" ")

print()  # salto de línea final