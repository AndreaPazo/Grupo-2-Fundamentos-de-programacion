
# Diseña la clase Producto(nombre, precio, stock) con métodos
# aplicar_descuento(%) y vender(cant). Lanza ValueError si no hay
# stock.
# Tip: implementa __str__ para print(producto)

#definir la clase Producto con los atributos nombre, precio y stock.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
 #definir el método aplicar_descuento que recibe un porcentaje y aplica el descuento al precio del producto.
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)
#definir el método vender que recibe una cantidad y reduce el stock del producto. Si la cantidad es mayor al stock disponible, lanza un ValueError.
    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock")
        self.stock -= cantidad
#def __str__(self):para representar el objeto Producto como una cadena de texto,
#  mostrando el nombre, precio y stock del producto.
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}, Stock: {self.stock}"


# Ejemplos de uso:
producto1 = Producto("Camiseta", 20.0, 50)
print(producto1)  # Producto: Camiseta, Precio: 20.00, Stock: 50

producto1.aplicar_descuento(10)  # Aplica un descuento del 10%
print(producto1)  # Producto: Camiseta, Precio: 18.00, Stock: 50

try:
    producto1.vender(60)  # Intenta vender 60 unidades (lanza ValueError)
except ValueError as e:
    print(e)  # No hay suficiente stock