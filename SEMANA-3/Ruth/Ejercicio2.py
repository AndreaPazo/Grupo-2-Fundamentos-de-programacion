#Crea una función es_par(numero) que retorne True si el número es par o False si es impar. Luego crea otra
#función mostrar_paridad(numero) (sin return) que use la primera función e imprima el resultado en pantalla
#con un mensaje.


def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))

mostrar_paridad(numero)

