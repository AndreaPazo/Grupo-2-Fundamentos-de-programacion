def contar_vocales(texto):

    vocales = "aeiouáéíóúü"

    contador = sum(
        1 for letra in texto.lower()
        if letra in vocales
    )

    return contador


print(contar_vocales("Hola José"))