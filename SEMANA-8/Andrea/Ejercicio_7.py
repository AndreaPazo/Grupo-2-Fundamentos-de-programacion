# Extracción con Expresiones Regulares
# Dada una lista de strings con información mezclada como:
# ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
# Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
# y almacénalos en una lista de diccionarios

import re

# Lista de strings con información mezclada
registros = [
    'Ana García - edad:25 - tel:987654321',
    'Luis Pérez - edad:30 - tel:912345678'
]

# Lista de diccionarios
personas = []

# Recorrer cada registro
for registro in registros:
    resultado = re.search(r'(.+?) - edad:(\d+) - tel:(\d+)', registro)

    if resultado:
        persona = {
            'nombre': resultado.group(1),
            'edad': int(resultado.group(2)),
            'telefono': resultado.group(3)
        }

        personas.append(persona)

# Mostrar la lista de diccionarios
print(personas)
