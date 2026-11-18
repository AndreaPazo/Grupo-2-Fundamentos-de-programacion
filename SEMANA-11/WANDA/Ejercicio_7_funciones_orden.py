#map() aplica la función lambda a cada elemento de la lista sin usar bucles for
celsius = [0, 10, 25, 37, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius)) #list() convierte el resultado de map en lista
print("Celsius -> Fahrenheit:", fahrenheit)

#filter() filtra y conserva solo los elementos donde la condición lambda es True
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros)) #evalúa si el residuo entre 2 es cero
print("Solo pares:", pares)

#sorted() ordena la lista de diccionarios usando el valor indicado en key
personas = [{"n": "Ana", "e": 30}, {"n": "Bob", "e": 22}, {"n": "Carla", "e": 27}]
por_edad = sorted(personas, key=lambda p: p["e"]) #lambda toma cada diccionario p y extrae su edad p["e"]
print("Ordenados por edad:", por_edad)
