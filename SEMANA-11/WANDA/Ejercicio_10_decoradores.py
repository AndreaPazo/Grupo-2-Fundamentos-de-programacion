import time
import functools #functools permite usar @wraps para conservar el nombre original de la función decorada


def cronometrar(func):
    #decorador que mide y muestra el tiempo de ejecución de cualquier función
    @functools.wraps(func) #evita que la función pierda su nombre real (__name__) al ser envuelta
    def wrapper(*args, **kwargs): #*args y **kwargs permiten recibir cualquier cantidad de argumentos
        inicio = time.perf_counter() #time.perf_counter() mide el tiempo con alta precisión en segundos
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"  [{func.__name__}{args}] tardó {fin - inicio:.6f} s")
        return resultado
    return wrapper


def memorizar(func):
    #decorador que guarda resultados previos en un diccionario (caché) para no recalcular
    cache = {} #diccionario donde la clave será el argumento (n,) y el valor su resultado

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache: #verifica si ese cálculo no está guardado aún en el diccionario
            cache[args] = func(*args) #si no existe, lo calcula y lo guarda en caché
        return cache[args] #devuelve el resultado guardado instantáneamente
    return wrapper


def fibonacci(n):
    #fibonacci recursivo SIN caché (repite los mismos cálculos muchas veces)
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memorizar #@memorizar aplica el decorador de caché automáticamente a fibonacci_memo
def fibonacci_memo(n):
    #fibonacci recursivo con caché (guarda cada resultado intermedio)
    if n < 2:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


#se cronometra desde afuera para que no imprima el tiempo en cada llamada recursiva interna
fib_sin_cache = cronometrar(fibonacci)
fib_con_cache = cronometrar(fibonacci_memo)


if __name__ == "__main__": #__name__ var que indica si se ejecuta este script directamente
    print("Sin caché:")
    print("  resultado:", fib_sin_cache(30))
    print("Con caché (1ra llamada):")
    print("  resultado:", fib_con_cache(30))
    print("Con caché (2da llamada):")
    print("  resultado:", fib_con_cache(30))
