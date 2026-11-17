
# Importa matematicas_utils con alias mu y crea
# reporte_geometrico(radios) que muestre área y perímetro de cada
# círculo en una tabla.

# Archivo: matematicas_utils.py
import math

def area_circulo(radio):
    return math.pi * (radio ** 2)

def perimetro_circulo(radio):
    return 2 * math.pi * radio