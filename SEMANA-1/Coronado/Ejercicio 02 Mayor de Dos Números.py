#int() convierte el texto ingresado en número entero
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Estructura condicional: evalúa en orden hasta que una condición sea verdadera
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los dos números son iguales")