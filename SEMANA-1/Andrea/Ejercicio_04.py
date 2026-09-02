# Contar y Sumar Pares del 1 al 20
# Usa una estructura Para para recorrer los números del 1 al 20. Por
# cada número par encontrado, incremente un contador y acumule la
# suma. Al finalizar muestra cuántos números pares hay y su suma total.

suma=0
contador=0

for i in range(1,21):
    if i % 2 == 0:
        contador += 1
        suma += i
        
print(f"Hay {contador} números pares")
print(f"La suma total es {suma}")