# CENSURAR PALABRA EN UN TEXTO:
# Dada una lista de palabras prohibidas, reemplaza cada aparición en un 
# texto por asteriscos del mismo largo

texto = "Esa pelicula es mala y el personaje es tonto y tramposo."

prohibidas = ["mala", "tonto", "tramposo"]

for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)