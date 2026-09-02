#================================================
#EJERCICIO 04 - CONTAR Y SUMAR PARES DEL 1 AL 20
#Estructura Repetitiva "Para" (for) + CONDICIONAL (if)
#==================================================

#inicia en 0 porque todavía no hemos contado ni sumado nada
contador_pares = 0
suma_pares = 0

#Se usa un bucle for para que recorra del 1 al 20 
#range(1, 21) -> del 1 al 20 ( 21 no se incluye)
for numero in range(1, 21):

    # Verificamos si el número es par
    # Un número es par cuando el resto de dividirlo entre 2 es 0
    if numero % 2 == 0:
        contador_pares = contador_pares + 1   # sumamos 1 al contador
        suma_pares = suma_pares + numero      # acumulamos el número a la suma

#Resultado
print("*****************************")
print(f"Cantidad de números pares encontrados: {contador_pares}")
print(f"Suma total de los números pares: {suma_pares}")