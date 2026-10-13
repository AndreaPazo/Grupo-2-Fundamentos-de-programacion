
# Combinación de Arreglos y Ordenamiento
# Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
# Combínalos en una lista de diccionarios, luego:
# 1) Ordena por ventas de mayor a menor.
# 2) Imprime el ranking con posición (1°, 2°, etc.).
# 3) Calcula el promedio de ventas e indica cuáles están sobre la media.

# 1. Definición de los arreglos paralelos de ejemplo
productos = ["Camisa Gorpcore", "Pantalón Cargo", "Zapatillas Trekking", "Gorra Urbana", "Chaqueta Impermeable"]
ventas = [45, 120, 85, 30, 95]

# Combinar los arreglos en una lista de diccionarios usando zip()
lista_productos = [
    {"producto": p, "ventas": v} for p, v in zip(productos, ventas)
]

# 1) Ordenar por ventas de mayor a menor (reverse=True)
lista_ordenada = sorted(lista_productos, key=lambda x: x["ventas"], reverse=True)

print("=" * 50)
print(f"{'RANKING DE VENTAS DE PRODUCTOS':^50}")
print("=" * 50)

# 2) Imprimir el ranking con posición (1°, 2°, etc.)
for posicion, item in enumerate(lista_ordenada, start=1):
    print(f"{posicion}° | Producto: {item['producto']:<22} | Ventas: {item['ventas']}")

print("-" * 50)

# 3) Calcular el promedio de ventas
promedio_ventas = sum(ventas) / len(ventas)
print(f"Promedio general de ventas: {promedio_ventas:.2f}")
print("-" * 50)

# Indicar cuáles están sobre la media
print("Productos que están sobre la media:")
for item in lista_ordenada:
    if item["ventas"] > promedio_ventas:
        print(f"  - {item['producto']} ({item['ventas']} ventas)")

print("=" * 50)