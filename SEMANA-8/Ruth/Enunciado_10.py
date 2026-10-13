

# Análisis de Texto y Estadísticas de Palabras
# Dado un párrafo de texto, implementa un analizador completo que:
# 1) Extraiga todas las palabras usando regex (solo letras y apóstrofes).
# 2) Construya un diccionario con la frecuencia de cada palabra (sin importar mayúsculas).
# 3) Ordene por frecuencia (desc) y luego alfabéticamente para desempates.
# 4) Muestre el top 5 de palabras más frecuentes y las palabras únicas ordenadas.


import re

def analizar_texto(parrafo):
    # 1. Extraer palabras usando regex
    palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ']+", parrafo)

    # 2. Convertir a minúsculas y contar frecuencias
    frecuencias = {}

    for palabra in palabras:
        palabra = palabra.lower()
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    # 3. Ordenar por frecuencia descendente y alfabéticamente
    ordenadas = sorted(
        frecuencias.items(),
        key=lambda elemento: (-elemento[1], elemento[0])
    )

    # 4. Mostrar resultados
    print("=" * 55)
    print("             ANALIZADOR DE TEXTO")
    print("=" * 55)

    print("\nTOP 5 PALABRAS MÁS FRECUENTES:")
    print("-" * 55)

    for palabra, frecuencia in ordenadas[:5]:
        print(f"- {palabra:<25}: {frecuencia}")

    # Palabras que aparecen una sola vez, ordenadas alfabéticamente
    unicas = sorted(
        palabra for palabra, frecuencia in frecuencias.items()
        if frecuencia == 1
    )

    print("\nPALABRAS ÚNICAS:")
    print("-" * 55)

    for palabra in unicas:
        print(f"- {palabra}")

    return frecuencias


# Texto de ejemplo
parrafo = """
Python es un lenguaje de programación. Python es fácil de aprender.
Aprender Python permite crear programas y analizar datos.
"""

frecuencias = analizar_texto(parrafo)
