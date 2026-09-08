# Escribe una función llamada calcular_descuento(precio, porcentaje) que reciba el precio original de
# un producto y el porcentaje de descuento, y retorne el precio final después del descuento. Luego
# muestra el ahorro obtenido

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje/100)
    precio_final = precio - descuento
    return precio_final

precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_final = calcular_descuento(precio, porcentaje)
ahorro = precio - precio_final

print(f"Ahorro obtenido: {ahorro}")
print(f"Precio final: {precio_final}")