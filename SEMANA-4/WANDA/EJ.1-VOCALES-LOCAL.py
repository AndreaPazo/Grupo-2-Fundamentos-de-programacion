def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    #conteo inicia al entrar aqui y se pierde al salir: no queda
    #rastro de el en el resto del programa
    conteo = 0
 
    for letra in texto:
        if letra in vocales:
            conteo += 1
 
    return conteo
 
print(contar_vocales("Hola Mundo"))  #4
 
#print(conteo)  #aca fallaria: conteo nunca existio fuera de la funcion
