# Importar módulo propio
# Importa matematicas_utils con alias mu y crea reporte_geometrico(radios) que muestre área y perímetro de cada círculo en una tabla.

# 1. Convertir Celsius a Fahrenheit usando map()

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print("Temperaturas en Fahrenheit:", fahrenheit)

# 2. filter() solo números pares 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# 3. Ordenar diccionarios por un campo usando sorted()

estudiantes = [
    {"nombre": "Andrea", "nota": 15},
    {"nombre": "Carlos", "nota": 18},
    {"nombre": "Lucia", "nota": 12}
]
ordenados = sorted(estudiantes, key=lambda x: x["nota"])
print("Estudiantes ordenados por nota:")
print(*ordenados, sep="\n")