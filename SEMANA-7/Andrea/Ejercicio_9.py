# ANALIZAR FRECUENCIA DE PALABRAS:
# Escribe una función que reciba un párrafo de texto y retorne un 
# diccionario con la frecuencia de cada palabra, ignorando signos de 
# puntuación, mayúsculas y palabras vacías (stopwords).

def analizar_frecuencia(texto):
    stopwords = ["el", "la", "los", "las", "un", "una", "de", "y", "en", "a"]

    # Convertir todo a minúsculas
    texto = texto.lower()

    # Eliminar signos de puntuación
    signos = ".,;:!?¿¡()[]\"'"

    for signo in signos:
        texto = texto.replace(signo, "")

    # Separar el texto en palabras
    palabras = texto.split()

    frecuencia = {}

    for palabra in palabras:
        if palabra not in stopwords:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

    return frecuencia


parrafo = "El perro corre y el perro juega. La casa es grande."
resultado = analizar_frecuencia(parrafo)

print(resultado)