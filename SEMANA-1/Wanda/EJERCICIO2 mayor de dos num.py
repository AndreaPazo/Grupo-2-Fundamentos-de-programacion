#======================================================
#EJERCICIO02 - CALCULA EL MAYOR DE DOS NÚMEROS
#Estructura condicional (Si - Sino)
#=======================================================

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

#Validar si son iguales, si es asì se muestra mensaje
if num1 == num2:
    print(f"Ambos números son iguales: {num1} = {num2}") 
#Si no son iguales, preguntamos cuál es mayor
elif num1 > num2:
    print(f"El número mayor es {num1}") 
#Si no se cumplió ninguna de las anteriores, entonces num2 es mayor
else:
    print(f"El número mayor es {num2}")
