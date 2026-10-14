# Registro de Productos con Arreglos Paralelos
# Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
# Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
# Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).

# Arreglos Paralelos
nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [2500.00, 45.00, 80.00, 650.00]
cantidades = [3, 10, 5, 2]

total_inventario = 0

print("REPORTE DE PRODUCTOS")
print("-" * 45)

for i in range(4):
    print(f"Producto: {nombres[i]} | Precio: S/ {precios[i]:.2f} | Stock: {cantidades[i]}")

    total_inventario += precios[i] * cantidades[i]

print("-" * 45)
print(f"Precio total del inventario: S/ {total_inventario:.2f}")
