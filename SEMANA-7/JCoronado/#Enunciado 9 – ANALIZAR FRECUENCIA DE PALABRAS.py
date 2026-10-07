def analizar_frecuencia(parrafo):
    # Lista de palabras vacías (stopwords) a ignorar durante el conteo
    stopwords = {"de", "el", "la", "los", "las", "un", "una", "y", "en", "con", "es"}
    
    # Lista de signos de puntuación comunes que deben eliminarse
    puntuacion = ".,;:!?()\"'"
    
    # Convierte todo el párrafo a minúsculas usando .lower()
    parrafo_minuscula = parrafo.lower()
    
    # Elimina los signos de puntuación reemplazando cada uno por una cadena vacía ""
    for signo in puntuacion:
        parrafo_minuscula = parrafo_minuscula.replace(signo, "")
    
    # Separa el texto limpio en una lista de palabras usando .split()
    palabras = parrafo_minuscula.split()
    
    # Inicializa un diccionario vacío para guardar el conteo de frecuencias
    frecuencia = {}
    
    # Iteración sobre cada palabra del texto
    for palabra in palabras:
        # Verifica que la palabra no esté en el conjunto de palabras vacías (stopwords)
        if palabra not in stopwords:
            # Si la palabra ya existe en el diccionario suma 1; si no, la crea con valor 1 mediante .get()
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
            
    # Retorna el diccionario con la frecuencia de palabras procesadas
    return frecuencia

# Ejemplo de uso de la función
texto_ejemplo = "El análisis de datos con Python es un análisis divertido y muy útil en la ciencia de datos."
resultado = analizar_frecuencia(texto_ejemplo)

# Imprime el diccionario resultante
print("Frecuencia de palabras:")
print(resultado)