#Saludo personalizado
# Crea una función saludar(nombre, saludo="Hola") que imprima
# "<saludo>, <nombre>!". Usa parámetro por defecto

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

# Ejemplo
saludar("Andrea")
saludar("Andrea", "Buenos días")