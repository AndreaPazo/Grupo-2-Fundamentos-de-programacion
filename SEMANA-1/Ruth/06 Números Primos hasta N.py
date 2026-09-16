#Solicita un número N y muestra todos los números
#primos desde 2 hasta N. Para cada número, verifica si
#es divisible entre 2 y hasta su raíz cuadrada.

numero = int(input("Ingrese un número N: "))

for n in range(2, numero + 1):
    es_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        print(n)