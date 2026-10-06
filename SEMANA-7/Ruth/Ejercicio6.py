

# CENSURAR PALABRA EN UN TEXTO:
# Dada una lista de palabras prohibidas, reemplaza cada aparición en un texto por asteriscos del mismo largo.

# Lista de palabras prohibidas

palabras_prohibidas = ["mala", "feo", "tonto"]

# Texto a censurar
texto = "la película fue mala y el final fue feo, pero no soy tonto para no entenderlo."

# Censurar las palabras prohibidas
for palabra in palabras_prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)
