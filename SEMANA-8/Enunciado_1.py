
# Registro de Productos con Arreglos Paralelos
# Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
# Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
# Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).

# 1. Creación de los tres arreglos paralelos para 4 productos
nombres = ["Camisa Gorpcore", "Pantalón Cargo", "Zapatillas Trekking", "Gorra Urbana"]
precios = [65.50, 110.00, 189.99, 35.00]
cantidades = [12, 8, 5, 20]

# 2. Imprimir el encabezado del reporte
print("=" * 45)
print(f"{'REPORTE DE INVENTARIO':^45}")
print("=" * 45)
print(f"{'PRODUCTO':<20} | {'PRECIO':<10} | {'STOCK':<6}")
print("-" * 45)

# Variable para acumular el costo total del inventario
inventario_total = 0

# 3. Recorrer los arreglos en paralelo usando un ciclo for
for i in range(len(nombres)):
    # Imprimir cada producto en una sola línea
    print(f"{nombres[i]:<20} | ${precios[i]:<9.2f} | {cantidades[i]:<6}")
    
    # 4. Calcular el precio total (precio × cantidad) de cada uno y sumarlo al total
    subtotal = precios[i] * cantidades[i]
    inventario_total += subtotal

print("-" * 45)
# Mostrar el resultado final del inventario completo
print(f"Precio total del inventario: ${inventario_total:.2f}")
print("=" * 45)