
# EXTRAER SUBCADENA:
# Dada la cadena 'Análisis de Datos con Python', extrae las palabras 'Datos' y 'Python' usando slicing.

cadena = "Análisis de Datos con Python"

# 1. Extraer 'Datos' (índices del 12 al 17)
datos = cadena[12:17]

# 2. Extraer 'Python' (desde el índice 21 hasta el final)
python = cadena[21:]

print(datos)   # Salida: Datos
print(python)  # Salida: Python