def calcular(a, b, operador):
    #Suma, resta, multiplica o divide si hay errores será none

    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            print("Error: no se puede dividir entre cero")
            return None
        return a / b
    else:
        print(f"Error: La operación '{operador}' no es válida")
        return None



print(calcular(8, 7, "+"))   #15
print(calcular(8, 3, "-"))   #5
print(calcular(6, 2, "*"))   #12
print(calcular(81, 4, "/"))   #20.25
calcular(45, 0, "/")          #error por división por cero
calcular(9, 2, "%")          #error es operador inválido
