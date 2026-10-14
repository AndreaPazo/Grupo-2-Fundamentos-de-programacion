# Análisis de Texto y Estadísticas de Palabras
# Dado un párrafo de texto, implementa un analizador completo que:
# 1) Extraiga todas las palabras usando regex (solo letras y apóstrofes).
# 2) Construya un diccionario con la frecuencia de cada palabra (sin importar mayúsculas).
# 3) Ordene por frecuencia (desc) y luego alfabéticamente para desempates.
# 4) Muestre el top 5 de palabras más frecuentes y las palabras únicas ordenadas.


import re

# Párrafo de texto
texto = """
Python es un lenguaje fácil de aprender.
Python permite analizar texto y procesar palabras.
Aprender Python es útil para programar y analizar datos.
"""

# 1. Extraer todas las palabras usando regex
palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ']+", texto)

# 2. Construir un diccionario con la frecuencia de cada palabra
frecuencias = {}

for palabra in palabras:
    palabra = palabra.lower()
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

# 3. Ordenar por frecuencia descendente y alfabéticamente
palabras_ordenadas = sorted(
    frecuencias.items(),
    key=lambda elemento: (-elemento[1], elemento[0])
)

# 4. Mostrar las 5 palabras más frecuentes
print("TOP 5 DE PALABRAS MÁS FRECUENTES")

for palabra, frecuencia in palabras_ordenadas[:5]:
    print(f"{palabra}: {frecuencia}")

# Mostrar las palabras únicas ordenadas alfabéticamente
palabras_unicas = sorted(
    [palabra for palabra, frecuencia in frecuencias.items() if frecuencia == 1]
)

print("\nPALABRAS ÚNICAS ORDENADAS")

for palabra in palabras_unicas:
    print(palabra)
