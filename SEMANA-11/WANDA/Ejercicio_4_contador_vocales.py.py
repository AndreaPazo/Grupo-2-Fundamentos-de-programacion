
def contar_vocales(texto):
    vocales = "aeiouáéíóúü"
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador

print(contar_vocales("Archipiélago AÉREO"))  
print(contar_vocales("Lambda"))            
