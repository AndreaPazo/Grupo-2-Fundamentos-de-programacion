# Calculadora básica
# Función calcular(a, b, operador) que soporte +, -, *, /. Retorna el
# resultado o None con mensaje de error si el operador no es válido o
# hay división por cero.

def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir entre cero")
            return None
    else:
        print("Error: Operador no válido")
        return None


# Ejemplos de uso
print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))
print(calcular(10, 0, "/"))
print(calcular(10, 5, "%"))