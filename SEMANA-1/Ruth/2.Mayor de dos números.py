#Solicita dos números enteros al usuario y determina cuál es el mayor. Si son iguales,indica que son iguales.
# Usa estructuras condicionales.


# Solicitar dos números enteros al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Determinar cuál es el mayor o si son iguales
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los números son iguales.")