# Definición de la cadena original con espacios en los extremos
cadena_original = "   Python es divertido "

# Elimina los espacios en blanco iniciales y finales usando .strip()
cadena_limpia = cadena_original.strip()

# Obtiene la cantidad de caracteres de la cadena limpia con la función len()
cantidad_caracteres = len(cadena_limpia)

# Muestra en pantalla la cadena sin espacios de borde y su longitud
print(f"Cadena limpia: '{cadena_limpia}'")
print(f"Número de caracteres: {cantidad_caracteres}")