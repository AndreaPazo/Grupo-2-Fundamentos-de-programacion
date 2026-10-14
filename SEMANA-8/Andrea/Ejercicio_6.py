# Combinación de Arreglos y Ordenamiento
# Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
# Combínalos en una lista de diccionarios, luego:
# 1) Ordena por ventas de mayor a menor.
# 2) Imprime el ranking con posición (1°, 2°, etc.).
# 3) Calcula el promedio de ventas e indica cuáles están sobre la media


# Arreglos paralelos
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [150, 300, 200, 100]

# Lista de diccionarios
lista_productos = []

for i in range(len(productos)):
    lista_productos.append({
        'producto': productos[i],
        'ventas': ventas[i]
    })

# 1. Ordenar por ventas de mayor a menor
lista_productos.sort(key=lambda producto: producto['ventas'], reverse=True)

# 2. Imprimir el ranking con posición
print("RANKING DE VENTAS")
for i in range(len(lista_productos)):
    print(f"{i + 1}°. {lista_productos[i]['producto']} - Ventas: {lista_productos[i]['ventas']}")

# 3. Calcular el promedio de ventas

prom = sum(ventas) / len(ventas)

print(f"\nPromedio de ventas: {prom:.2f}")

# indicar cuáles están sobre la media
print("Productos con ventas sobre la media:")

for producto in lista_productos:
    if producto['ventas'] > prom:
        print(f"{producto['producto']} - Ventas: {producto['ventas']}")
