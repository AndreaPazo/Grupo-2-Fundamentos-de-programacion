import math

def area_circulo(radio):

    if radio < 0:
        raise ValueError("Radio negativo")

    return math.pi * radio ** 2


def perimetro_circulo(radio):

    if radio < 0:
        raise ValueError("Radio negativo")

    return 2 * math.pi * radio


def reporte_geometrico(radios):

    return [
        {
            "radio": radio,
            "area": area_circulo(radio),
            "perimetro": perimetro_circulo(radio)
        }
        for radio in radios
    ]