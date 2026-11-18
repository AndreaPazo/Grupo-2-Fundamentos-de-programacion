#Este ejercicio utiliza:
#Decoradores con @.
#functools.wraps.
#time.perf_counter() para medir tiempos.
#Diccionarios para guardar resultados.
#Fibonacci recursivo con y sin caché.
import time
from functools import wraps


# DECORADOR 1: CRONOMETRAR TIEMPO
def cronometro(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        inicio = time.perf_counter()

        resultado = func(*args, **kwargs)

        fin = time.perf_counter()

        tiempo = fin - inicio

        print(f"Funcion: {func.__name__}")
        print(f"Tiempo de ejecucion: {tiempo:.8f} segundos")

        return resultado

    return wrapper


# DECORADOR 2: MEMOIZACION (CACHE)
def memorizar(func):

    cache = {}

    @wraps(func)
    def wrapper(*args):

        if args not in cache:

            cache[args] = func(*args)

        return cache[args]

    return wrapper


# FIBONACCI SIN MEMOIZACION
@cronometro
def fibonacci_sin_cache(n):

    if n <= 1:
        return n

    return (
        fibonacci_sin_cache.__wrapped__(n - 1)
        + fibonacci_sin_cache.__wrapped__(n - 2)
    )


# FIBONACCI CON MEMOIZACION
@cronometro
@memorizar
def fibonacci_con_cache(n):

    if n <= 1:
        return n

    return (
        fibonacci_con_cache(n - 1)
        + fibonacci_con_cache(n - 2)
    )


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    numero = 30

    print("===================================")
    print(" FIBONACCI SIN MEMOIZACION")
    print("===================================")

    inicio = time.perf_counter()

    resultado1 = fibonacci_sin_cache(numero)

    fin = time.perf_counter()

    print("Resultado:", resultado1)
    print(f"Tiempo total: {fin - inicio:.8f} segundos")

    print("\n===================================")
    print(" FIBONACCI CON MEMOIZACION")
    print("===================================")

    inicio = time.perf_counter()

    resultado2 = fibonacci_con_cache(numero)

    fin = time.perf_counter()

    print("Resultado:", resultado2)
    print(f"Tiempo primera llamada: {fin - inicio:.8f} segundos")

    print("\n===================================")
    print(" SEGUNDA LLAMADA CON CACHE")
    print("===================================")

    inicio = time.perf_counter()

    resultado3 = fibonacci_con_cache(numero)

    fin = time.perf_counter()

    print("Resultado:", resultado3)
    print(f"Tiempo segunda llamada: {fin - inicio:.8f} segundos")

    print("\n===================================")
    print(" COMPARACION FINALIZADA")
    print("===================================")
