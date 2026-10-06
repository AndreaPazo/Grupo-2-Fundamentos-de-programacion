

# ANALIZAR FRECUENCIA DE PALABRAS:
# Escribe una función que reciba un párrafo de texto y retorne un diccionario con la frecuencia de cada palabra,
# ignorando signos de puntuación, mayúsculas y palabras vacías (stopwords)


def analizar_frecuencia(texto):
    # Convertir a minúsculas y eliminar signos de puntuación
    texto = texto.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    
    # Dividir en palabras
    palabras = texto.split()
    
    # Eliminar palabras vacías
    stopwords = {"el", "la", "de", "en", "y", "o", "pero", "a", "que", "se", "por", "con", "para", "sin", "sobre", "entre", "hacia", "durante", "desde", "hasta", "antes", "después", "cuando", "donde", "porqué", "cómo", "quiénes", "cuáles", "cuántos", "cuántas"}
    palabras = [palabra for palabra in palabras if palabra not in stopwords]
    
    # Contar frecuencia
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

parrafo = "Siempre es un buen momento para aprender a programar. La programación es una habilidad valiosa y divertida. ¡Aprender a programar puede abrir muchas puertas!"

resultado = analizar_frecuencia(parrafo)

print(resultado)