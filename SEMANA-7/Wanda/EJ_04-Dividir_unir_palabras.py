
#EJ:'rojo,verde,azul,amarillo' ~  separar, mayúsculas, unir con ' | '
color_texto = "rojo,verde,azul,amarillo"
lista_colores = color_texto.split(",")   #split() separa el texto y crea una lista.

color_mayus = []                         #lista vacía para guardar los resultados
for color in lista_colores:                #recorre cada color
    color_mayus.append(color.upper())    #convierte cada color a mayúsculas y lo agrega (appd)

resultado = " | ".join(color_mayus)      #join() une la lista con el separador
print(resultado)   #Imprime: ROJO | VERDE | AZUL | AMARILLO

