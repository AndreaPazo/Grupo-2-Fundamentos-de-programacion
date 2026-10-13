
#  Extracción con Expresiones Regulares
# Dada una lista de strings con información mezclada como:
# ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
# Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
# y almacénalos en una lista de diccionarios.


import re

# Lista de strings con información mezclada (incluyendo posibles saltos de línea o espacios)
registros = [
    'Ana García - edad:25 - tel:987654321', 
    'Luis Pérez - edad:30 - tel:912345678'
]

# Lista donde guardaremos los diccionarios resultantes
lista_diccionarios = []

# Expresión regular explicada:
# (.+?)  -> Grupo 1: Captura el nombre (cualquier texto de forma no codiciosa)
# \s*-\s*edad:(\d+) -> Captura el separador y el Grupo 2: Dígitos de la edad
# \s*-\s*tel:(\d+)  -> Captura el separador y el Grupo 3: Dígitos del teléfono
patron = re.compile(r"^(.+?)\s*-\s*edad:(\d+)\s*-\s*tel:(\d+)")


for registro in registros:
    # Normalizamos la cadena eliminando saltos de línea por si los tuviera
    registro_limpio = registro.replace("\n", " ").strip()
    
    match = patron.search(registro_limpio)
    
    if match:
        # Extraemos los grupos capturados por la expresión regular
        nombre = match.group(1).strip()
        edad = int(match.group(2))
        telefono = match.group(3)
        
        # Creamos el diccionario y lo agregamos a la lista
        info_estudiante = {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }
        lista_diccionarios.append(info_estudiante)

# Mostrar el resultado final estructurado
print("Lista de diccionarios extraída:")
for d in lista_diccionarios:
    print(d)