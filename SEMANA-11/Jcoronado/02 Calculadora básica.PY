def calcular(a, b, operador):

    if operador == "+":
        return a + b

    elif operador == "-":
        return a - b

    elif operador == "*":
        return a * b

    elif operador == "/":
        if b == 0:
            print("Error: división entre cero")
            return None
        return a / b

    else:
        print("Operador no válido")
        return None


print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))