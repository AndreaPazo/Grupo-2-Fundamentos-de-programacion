class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):

        if not 0 <= porcentaje <= 100:
            raise ValueError("Descuento inválido")

        self.precio *= (1 - porcentaje / 100)

    def vender(self, cantidad):

        if cantidad <= 0:
            raise ValueError("Cantidad inválida")

        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente")

        self.stock -= cantidad

        return cantidad * self.precio


producto = Producto("Teclado", 100, 10)

producto.aplicar_descuento(15)

total = producto.vender(2)

print("Precio:", producto.precio)
print("Total de venta:", total)
print("Stock restante:", producto.stock)