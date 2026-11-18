import math
from abc import ABC, abstractmethod #ABC permite crear clases abstractas que sirven de molde


class Figura(ABC):
    #clase base abstracta: obliga a que sus clases hijas implementen area() y perimetro()
    @abstractmethod #@abstractmethod decorador que indica que este método es obligatorio en las subclases
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def describir(self):
        #self.__class__.__name__ obtiene automáticamente el nombre de la clase hija (Circulo, Rectangulo, etc.)
        return (f"{self.__class__.__name__:<10} "
                f"Área: {self.area():8.2f} | Perímetro: {self.perimetro():8.2f}")


class Circulo(Figura): #hereda de Figura
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(Figura): #hereda de Figura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura): #hereda de Figura
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        #fórmula de Herón: s = semiperímetro
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def comparar_figuras(lista):
    #ordena las figuras por área de mayor a menor (reverse=True) usando polimorfismo
    ordenadas = sorted(lista, key=lambda f: f.area(), reverse=True) #lambda extrae el área de cada figura f
    for f in ordenadas:
        print(f.describir())


if __name__ == "__main__": #__name__ var que indica si se ejecuta este script directamente
    figuras = [Circulo(5), Rectangulo(4, 3), Triangulo(3, 4, 5), Rectangulo(10, 10)]
    comparar_figuras(figuras)
