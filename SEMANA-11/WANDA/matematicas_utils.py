# archivo: matematicas_utils.py
PI = 3.14159  # constante


def area_circulo(r):
    """Área de un círculo."""
    return PI * r ** 2


def perimetro_circulo(r):
    """Perímetro (circunferencia) de un círculo."""
    return 2 * PI * r


def es_primo(n):
    """Devuelve True si n es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Solo corre al ejecutar este archivo directamente
if __name__ == "__main__":
    print(area_circulo(5))
    print(es_primo(7))
