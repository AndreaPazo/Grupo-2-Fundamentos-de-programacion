# Texto de entrada del tweet
tweet = "Aprendiendo #Python y #DataScience con los mejores ejercicios de #Programacion!"

# Divide el tweet en una lista de palabras individuales usando .split() (por defecto espacios)
palabras = tweet.split()

# Lista vacía donde se almacenarán los hashtags encontrados
hashtags = []

# Recorre cada palabra obtenida del tweet
for palabra in palabras:
    # Comprueba si la palabra comienza con el carácter '#' mediante .startswith('#')
    if palabra.startswith("#"):
        # Limpia signos de puntuación pegados al final (como '!') usando .strip() y pasa a minúsculas con .lower()
        hashtag_limpio = palabra.strip("!?,.").lower()
        
        # Agrega el hashtag procesado a la lista
        hashtags.append(hashtag_limpio)

# Ordena alfabéticamente la lista de hashtags con el método .sort()
hashtags.sort()

# Muestra la lista final de hashtags extraídos y ordenados
print(f"Hashtags extraídos: {hashtags}")