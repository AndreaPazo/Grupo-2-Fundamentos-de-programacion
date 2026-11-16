
# Función calcular(a, b, operador) que soporte +, -, *, /. Retorna el
# resultado o None con mensaje de error si el operador no es válido o
# hay división por cero

def calcular(a, b, operador):
  if operador == "+":
    return a + b
  elif operador == "-":
    return a - b
  elif operador == "*":
    return a * b
  elif operador == "/":
    if b == 0:
      print("Error: División por cero")
      return None
    return a / b
  else:
    print("Error: Operador no válido")
    return None


# Ejemplos de prueba (sin indentación):
print(calcular(10, 5, "+"))  # 15
print(calcular(10, 5, "-"))  # 5
print(calcular(10, 5, "*"))  # 50
print(calcular(10, 5, "/"))  # 2.0
print(calcular(10, 0, "/"))  # Error: División por cero -> None
print(calcular(10, 5, "%"))  # Error: Operador no válido -> None