#Ej.1 contar_vocales que reciba un texto como parámetro y devuelva el número total de vocales que contiene (sin importar si son mayúsculas o minúsculas)

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0       # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo

print(contar_vocales("murcielago")) #4