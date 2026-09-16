# Crea una función es_par(numero) que retorne True si el número es par o False si es impar. 
# Luego crea otra función mostrar_paridad(numero) (sin return) que use la primera función e 
# imprima el resultado en pantalla con un mensaje

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def mostrar_paridad(num):
    if es_par(num):
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")


numeros = [2, 5, 8, 11, 14]

for num in numeros:
    mostrar_paridad(num)