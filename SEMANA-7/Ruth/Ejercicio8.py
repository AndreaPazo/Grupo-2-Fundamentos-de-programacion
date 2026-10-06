

# EXTRAER HASHTAGS DE UN TWEET:
# Dado un texto de tweet, extrae todos los hashtags (#palabras) y devuélvelos en una lista ordenada y en minúsculas.


#extensión de la función para extraer hashtags
import re


# Función para extraer hashtags de un tweet
def extraer_hashtags(tweet):
    hashtags = re.findall(r"#\w+", tweet)
    hashtags = sorted([hashtag.lower() for hashtag in hashtags])
    return hashtags

tweet = "Hoy fue un gran día! #Perú #Python #Programación #Tecnología"

resultado = extraer_hashtags(tweet)

print(resultado)