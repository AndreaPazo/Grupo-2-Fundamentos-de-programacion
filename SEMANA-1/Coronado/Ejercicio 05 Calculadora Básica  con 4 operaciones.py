num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

match operador:
    case "+":
        print(f"Resultado: {num1 + num2:.2f}")
    case "-":
        print(f"Resultado: {num1 - num2:.2f}")
    case "*":
        print(f"Resultado: {num1 * num2:.2f}")
    case "/":
        if num2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            print(f"Resultado: {num1 / num2:.2f}")
    case _:
        print("Operador no válido")