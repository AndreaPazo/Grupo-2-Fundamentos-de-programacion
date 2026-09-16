

#Usa una estructura Para para recorrer los números del 1 al 20. 
# Por cadanúmero par encontrado, incremente un contador y acumule la suma.
#Al finalizar muestra cuántos números pares hay y su suma total.

# Inicializar contador y suma
contador_pares = 0
suma_pares = 0

# Recorrer los números del 1 al 20
for numero in range(1, 21):
    if numero % 2 == 0:  # Verificar si el número es par
        contador_pares += 1
        suma_pares += numero

# Mostrar los resultados
print(f"El número de pares es: {contador_pares}")
print(f"La suma de los pares es: {suma_pares}")