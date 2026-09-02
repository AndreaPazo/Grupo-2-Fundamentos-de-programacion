# Mayor de Dos Números
# Solicita dos números enteros al usuario y determina cuál es el mayor. Si son iguales,
# indica que son iguales. Usa estructuras condicionales

num1 = int(input("Ingrese el primer número entero: "))  
num2 = int(input("Ingrese el segundo número entero: "))  

if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")