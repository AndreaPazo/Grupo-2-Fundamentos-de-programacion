#Ej.2 celsius_a_fahrenheit que reciba una temperatura en grados Celsius como parámetro y devuelva su equivalente en grados Fahrenheit.
def celsius_a_fahrenheit(c):
    factor = 9 / 5 # Variablelocal
    fahrenheit = c * factor + 32 # Variablelocal
    return fahrenheit

print(celsius_a_fahrenheit(100)) # imprime:212.0
print(celsius_a_fahrenheit(0)) # imprime:32.0