
from abc import ABC, abstractmethod
import math


# CLASE BASE ABSTRACTA
class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# SUBCLASE CIRCULO
class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


# SUBCLASE RECTANGULO
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# SUBCLASE TRIANGULO
class Triangulo(Figura):

    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Los lados no forman un triangulo valido")

        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        # Formula de Heron
        s = self.perimetro() / 2

        return math.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )


# FUNCION POLIMORFICA PARA ORDENAR FIGURAS
def ordenar_figuras(figuras):

    return sorted(
        figuras,
        key=lambda figura: figura.area(),
        reverse=True
    )


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    figuras = [
        Circulo(5),
        Rectangulo(8, 4),
        Triangulo(3, 4, 5),
        Circulo(3),
        Rectangulo(6, 6)
    ]

    figuras_ordenadas = ordenar_figuras(figuras)

    print("===================================")
    print(" SISTEMA DE FIGURAS GEOMETRICAS")
    print("===================================")

    print("\nFIGURAS ORDENADAS POR AREA (MAYOR A MENOR)\n")

    for figura in figuras_ordenadas:

        print("Figura:", figura.__class__.__name__)
        print("Area:", round(figura.area(), 2))
        print("Perimetro:", round(figura.perimetro(), 2))
        print("-----------------------------------")
#Este ejercicio utiliza:
#ABC y abstractmethod.
#Herencia y polimorfismo.
#Clases Circulo, Rectangulo y Triangulo.
#Cálculo de áreas y perímetros.
#Ordenamiento de figuras de mayor a menor área.