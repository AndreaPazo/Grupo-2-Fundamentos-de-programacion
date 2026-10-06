
#LIMPIAR Y CONTAR:
# Dada la cadena ' Python es divertido ', elimina los espacios en los extremos y cuenta cuántos caracteres tiene la
# cadena limpia.

# Cadena original
cadena = " Python es divertido "

# 1. Limpiar los espacios en los extremos con strip()
cadena_limpia = cadena.strip()

# 2. Contar los caracteres con len()
cantidad_caracteres = len(cadena_limpia)

print(f"Cadena limpia: '{cadena_limpia}'")
print(f"Número de caracteres: {cantidad_caracteres}")