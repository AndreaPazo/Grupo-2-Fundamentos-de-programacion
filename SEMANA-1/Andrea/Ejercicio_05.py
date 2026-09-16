# Calculadora Básica (4 operaciones)
# Solicita dos números y un operador (+, -, *, /). Usa una estructura Según para determinar la operación. 
# Maneja el caso de división por cero con una condicional

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")   
elif operador == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: División por cero no permitida.")

else:
    print("Operador no válido")