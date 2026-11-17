
# Sin for/while: usa map() para convertir Celsius→Fahrenheit, filter()
# para solo pares, sorted() con lambda para ordenar dicts por campo.
# Tip: list(map(lambda x: ..., lista)) — sin bucles explícitos.

# 1. Convertir Celsius a Fahrenheit usando map()
celsius = [0, 15, 25, 30, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)  # [32.0, 59.0, 77.0, 86.0, 212.0]

# 2. Filtrar solo números pares usando filter()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números:", numeros)
print("Pares:", pares)  # [2, 4, 6, 8, 10]

# 3. Ordenar lista de diccionarios por un campo usando sorted() + lambda
productos = [
    {"nombre": "Teclado", "precio": 45.0},
    {"nombre": "Mouse", "precio": 20.0},
    {"nombre": "Monitor", "precio": 220.0},
]   

ordenados_por_precio = sorted(productos, key=lambda p: p["precio"])
print("Productos ordenados por precio:", ordenados_por_precio)