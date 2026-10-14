# Búsqueda y Filtrado de Productos
# Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
# Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
# cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
# Además, ordena los resultados por precio de menor a mayor.

productos = [
    {'nombre': 'Laptop Lenovo', 'categoria': 'Computadoras', 'precio': 2500.00},
    {'nombre': 'Mouse Logitech', 'categoria': 'Accesorios', 'precio': 80.00},
    {'nombre': 'Laptop HP', 'categoria': 'Computadoras', 'precio': 2200.00},
    {'nombre': 'Teclado Logitech', 'categoria': 'Accesorios', 'precio': 120.00},
    {'nombre': 'Mouse Microsoft', 'categoria': 'Accesorios', 'precio': 65.00}
]

def buscar_productos(lista, termino):
    resultados = []

    for producto in lista:
        if termino.lower() in producto['nombre'].lower():
            resultados.append(producto)

    #ordena los resultados por precio de menor a mayor.
    resultados.sort(key=lambda producto: producto['precio'])

    return resultados


# Buscar productos
termino = input("Ingrese el nombre del producto que desea buscar: ")
resultados = buscar_productos(productos, termino)

# Mostrar resultados
print("\nPRODUCTOS ENCONTRADOS")

if resultados:
    for producto in resultados:
        print(f"Nombre: {producto['nombre']} | Categoría: {producto['categoria']} | Precio: S/ {producto['precio']:.2f}")
else:
    print("No se encontraron productos.")
