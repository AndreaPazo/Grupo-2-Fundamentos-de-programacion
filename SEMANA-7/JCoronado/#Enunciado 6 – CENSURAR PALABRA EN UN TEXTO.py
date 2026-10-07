# Texto de entrada original
texto = "Este es un examen de prueba con palabras secretas y datos confidenciales."

# Lista de palabras que se deben censurar
palabras_prohibidas = ["examen", "secretas", "confidenciales"]

# Inicia un bucle para iterar sobre cada palabra prohibida en la lista
for palabra in palabras_prohibidas:
    # Genera una cadena de asteriscos '*' multiplicados por la longitud de la palabra
    censura = "*" * len(palabra)
    
    # Reemplaza todas las apariciones de la palabra prohibida por los asteriscos usando .replace()
    texto = texto.replace(palabra, censura)

# Muestra el texto resultante con las palabras reemplazadas por asteriscos
print(f"Texto censurado: {texto}")