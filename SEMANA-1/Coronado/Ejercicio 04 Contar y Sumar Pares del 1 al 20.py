contador = 0
suma = 0

for numero in range(1, 21):
    if numero % 2 == 0:   # % es el operador módulo: da el resto de una división
        contador += 1     # contador += 1 es lo mismo que contador = contador + 1
        suma += numero

print(f"Cantidad de números pares: {contador}")
print(f"Suma total de los pares: {suma}")