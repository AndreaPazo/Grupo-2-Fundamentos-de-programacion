def celsius_a_fahrenheit(c):
    factor = 9 / 5
    fahrenheit = c * factor + 32
    return fahrenheit
 
 
print(celsius_a_fahrenheit(100))  #212.0
print(celsius_a_fahrenheit(0))    #32.0
 
#aca'factor' aqui es independiente de cualquier otra variable llamada
#al igual en otra funcion del programa, porque cada funcion tiene su
#propio espacio de nombres
 
