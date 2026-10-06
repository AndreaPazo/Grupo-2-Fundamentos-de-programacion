#Lista ordenada y en minúsculas

tweet = "Sobreviviendo a los proyectos #Python #Programacion #Universidad"

hashtags = []

#split() separa el tweet en palabras
for palabra in tweet.split():
    if palabra.startswith("#"):#startswith() comprueba si la palabra empieza con #
        hashtags.append(palabra.lower()) #hashtag a mins y agrega a la lista

#sort() ordena la lista alfabéticamente
hashtags.sort()

print(hashtags)


