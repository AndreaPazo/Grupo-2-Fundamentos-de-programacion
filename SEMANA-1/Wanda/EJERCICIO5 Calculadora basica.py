#========================================
#EJERCICIO 05 - CALCULADORA BÁSICA (4 OPERACIONES)
#Estructura mediante if/elif (comparaciones)
#=========================================
#Datos ingresados
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese la operación (+, -, *, /): ")

#Se compara de acuerdo al operador
if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif operador == "/":
    # Caso especial: no se puede dividir entre 0
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")

#Si ninguno de los operadores es válido, se muestra un mensaje de error
else:
    print("Operador no válido. Use +, -, * o /")