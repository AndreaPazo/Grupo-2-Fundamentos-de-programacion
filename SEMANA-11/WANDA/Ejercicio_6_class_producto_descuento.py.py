class Producto:
    #define un producto con nombre,precio y stock
    def __init__(self, nombre, precio, stock): #__init__ constructor que inicializa los atributos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, pct):
        #reduce el precio aplicando el porcentaje de descto
        self.precio *= (1 - pct / 100)

    def vender(self, cantidad):
        #verifica si hay stock suficiente antes de descontar y cobrar
        if cantidad > self.stock:
            raise ValueError("Sin stock") #raise lanza una excepción manual si falta stock
        self.stock -= cantidad
        return self.precio * cantidad

    def __str__(self): #__str__ define cómo se muestra el objeto al usar print()
        return f"[{self.nombre}] S/.{self.precio:.2f} (stock: {self.stock})"


if __name__ == "__main__": #__name__ var que indica si se ejecuta este script directamente
    p = Producto("Laptop", 2500, 10)
    p.aplicar_descuento(15)
    total = p.vender(2)
    print(p)
    print(f"Total de la venta: S/.{total:.2f}")

    try: #try intenta ejecutar un code que puede fallar
        p.vender(100)
    except ValueError as e: #except captura el error lanzado por raise sin detener el programa
        print("Error:", e)
