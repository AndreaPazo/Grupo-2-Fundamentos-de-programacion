# Clase Producto con descuento
# Diseña la clase Producto(nombre, precio, stock) con métodos aplicar_descuento(%) y vender(cant). Lanza ValueError si no hay stock.

class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Aplicar descuento (%)
    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)

    # Vender productos
    def vender(self, cant):
        if cant > self.stock:
            raise ValueError("No hay suficiente stock disponible")

        self.stock -= cant
        print(f"Se vendieron {cant} unidades de {self.nombre}")

    # Mostrar información del producto
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: S/ {self.precio:.2f} | Stock: {self.stock}"

# Crear un producto
producto = Producto("Laptop", 2500, 10)
print(producto)

# Aplicar 10% de descuento
producto.aplicar_descuento(10)
print("Después del descuento:")
print(producto)

# Vender 3 unidades
producto.vender(3)
print(producto)