# EXTRAER HASHTAGS DE UN TWEET:
# Dado un texto de tweet, extrae todos los hashtags (#palabras) 
# y devuélvelos en una lista ordenada y en minúsculas.

def extraer_hashtags(tweet):
    palabras = tweet.split()
    hashtags = []

    for palabra in palabras:
        if palabra.startswith("#"):
            hashtags.append(palabra.lower())

    hashtags.sort()

    return hashtags


tweet = "Hoy aprendí Python #Programacion #Python y practiqué mucho #codigo"
resultado = extraer_hashtags(tweet)
print(resultado)