

# DIVIDIR Y UNIR PALABRAS:
# Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, ponlos en mayúsculas y únelos con ' | ' como separador.


cadena = "rojo,verde,azul,amarillo"

colores = cadena.split(",")
resultado = " | ".join(color.upper() for color in colores)

print(resultado)