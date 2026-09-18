# Separa la lógica matemática en un archivo propio (matematicas.py) para poder reusarla en otros proyectos sin duplicar código.

def sumar(a, b): 
    return a + b  # Retorna la suma de dos números.

def restar(a, b): 
    return a - b  # Retorna la resta de dos números.

def multiplicar(a, b): 
    return a * b  # Retorna la multiplicación de dos números.

def dividir(a, b):
    if b == 0: 
        raise ValueError("División por cero")  # Lanza un error si el divisor es 0 para evitar fallos del sistema.
    return a / b  # Retorna la división (en Python siempre devuelve un float).

# IMPORTACIÓN SELECTIVA: Trae ÚNICAMENTE las funciones 'sumar' y 'dividir' del módulo 'matematicas'.
# Las funciones 'restar' y 'multiplicar' quedan fuera del alcance de main.py, optimizando memoria y legibilidad.
from matematicas import sumar, dividir

print(sumar(10, 5))    # Llama a sumar(10, 5) -> Imprime: 15
print(dividir(20, 4))  # Llama a dividir(20, 4) -> Imprime: 5.0