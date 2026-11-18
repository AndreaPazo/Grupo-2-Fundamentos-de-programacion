
def clasificar_temperatura(temp):
    #T° de acuerdo a los siguientes rangos
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"

for t in (-2, 5, 10, 15, 20, 25, 30, 35.5):
    print(f"{t}°C -> {clasificar_temperatura(t)}")