# Convertir Celsius a Fahrenheit

celsius = [0, 10, 20, 25, 30]

fahrenheit = list(
    map(lambda c: (c * 9/5) + 32, celsius)
)

print(fahrenheit)


# Obtener solamente números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = list(
    filter(lambda x: x % 2 == 0, numeros)
)

print(pares)


# Ordenar productos por precio

productos = [
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Mouse", "precio": 45},
    {"nombre": "Monitor", "precio": 650}
]

ordenados = sorted(
    productos,
    key=lambda x: x["precio"]
)

print(ordenados)