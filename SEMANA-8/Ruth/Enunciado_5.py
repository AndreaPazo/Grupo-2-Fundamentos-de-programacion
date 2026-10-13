
# Búsqueda y Filtrado de Productos
# Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
# Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
# cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
# Además, ordena los resultados por precio de menor a mayor.


productos = [
    {"nombre": "Laptop Lenovo", "categoria": "Tecnología", "precio": 2500},
    {"nombre": "Mouse Logitech", "categoria": "Accesorios", "precio": 80},
    {"nombre": "Laptop HP", "categoria": "Tecnología", "precio": 2200},
    {"nombre": "Teclado mecánico", "categoria": "Accesorios", "precio": 150},
    {"nombre": "Mouse inalámbrico", "categoria": "Accesorios", "precio": 50}
]

def buscar_productos(lista, termino):
    resultados = []

    for producto in lista:
        if termino.lower() in producto["nombre"].lower():
            resultados.append(producto)

    resultados.sort(key=lambda producto: producto["precio"])

    return resultados

# Buscar productos
busqueda = input("Ingrese el nombre del producto que desea buscar: ")

encontrados = buscar_productos(productos, busqueda)

if encontrados:
    print("\nProductos encontrados:")
    for producto in encontrados:
        print(producto["nombre"], "-", producto["categoria"],
              "- S/", producto["precio"])
else:
    print("-" * 45)
    print("No se encontraron productos.")
