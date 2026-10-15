
#EJERCICIO 1 - Registro de productos con arreglos paralelos
print("=" * 60)
print("EJERCICIO 1 - Registro de productos")
print("=" * 60)
 
#Tres listas del MISMO tamaño
nombres = ['Laptop', 'Mouse', 'Teclado', 'Monitor']   # Lista 1
precios = [2500.0, 50.0, 120.0, 800.0]                # Lista 2
cantidades = [15, 40, 25, 10]                         # Lista 3
 
total_inventario = 0

#bucle for y amarro las 3 listas con func zip
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    print(f"{nombre}: S/ {precio:.1f} - Stock: {cantidad}")
    total_inventario += precio * cantidad
 
print(f"Precio total del inventario: S/ {total_inventario:.1f}")
 
