#recibe un párrafo y retorna un diccionario
# {palabra: veces}, ignorando puntuación, mayúsculas y stopwords

def frec_palabras(parrafo):

    #Lista de palabras vacías que no queremos contar
    stopwords = [
        "la", "el", "con" ,"nos", "los", "las", "una", "un",
        "y", "para", "son", "es", "de", "del"
    ]
    #Convertir todo el texto a minúsculas
    parrafo = parrafo.lower()
  
    #Eliminar los signos de puntuación
    for signo in [".", ",", ";", ":", "!", "?", "¡", "¿"]:
        parrafo = parrafo.replace(signo, "")

    #Separa el párrafo en palabras
    palabras = parrafo.split()

    #Crea un diccionario vacío para guardar las frecuencias
    frecuencias = {}

    #Recorre cada palabra del párrafo
    for palabra in palabras:

        #Ignoramos las palabras que están en stopwords
        if palabra not in stopwords:

            #Si la palabra ya existe, aumentamos su contador
            #Si no existe, empezamos desde 0
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    #Retornamos el diccionario con las frecuencias
    return frecuencias
#Cadena
parrafo = """
La programación con python nos permite desarrollar soluciones eficientes para resolver problemas complejos
Los algoritmos y las estructuras de datos son fundamentales para crear software eficiente y confiable
Una buena programación nos facilita el mantenimiento del código y permite desarrollar aplicaciones escalables
"""
print(frec_palabras(parrafo))

