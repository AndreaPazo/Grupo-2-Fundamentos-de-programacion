# Función clasificar_temperatura(temp) que retorne "Frío" (<10),
# "Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30).
# Tip: encadena elif con los rangos del enunciado


def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"

# Ejemplos de prueba (sin indentación):
print(clasificar_temperatura(5))   # Frío   
print(clasificar_temperatura(15))  # Fresco
print(clasificar_temperatura(25))  # Cálido
print(clasificar_temperatura(30))  # Caliente



