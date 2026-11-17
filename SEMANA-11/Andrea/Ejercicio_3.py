# Clasificador de temperatura
# Función clasificar_temperatura(temp) que retorne "Frío" (<10),
# "Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30)

def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"


# Ejemplos de uso
print(clasificar_temperatura(5))
print(clasificar_temperatura(15))
print(clasificar_temperatura(25))
print(clasificar_temperatura(35))