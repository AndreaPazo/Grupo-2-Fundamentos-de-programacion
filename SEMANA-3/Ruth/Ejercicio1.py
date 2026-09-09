#Escribe una función llamada calcular_descuento(precio, porcentaje) que reciba el precio original de
#un producto y el porcentaje de descuento, y retorne el precio final después del descuento. Luego
#muestra el ahorro obtenido


def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

# Ejemplo de uso
precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Calcular el precio final y el ahorro


precio_final = calcular_descuento (precio_original,porcentaje_descuento)
ahorro = precio_original - precio_final



# Mostrar los resultados
print(f"El precio final después del descuento es: {precio_final}")
print(f"El ahorro obtenido es: {ahorro}")
