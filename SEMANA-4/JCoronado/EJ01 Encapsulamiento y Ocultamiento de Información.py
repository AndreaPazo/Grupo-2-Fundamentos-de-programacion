#Cuál es el resultado de ejecutar el script y qué sucede si intentas acceder directamente al atributo c.__saldo desde fuera de la clase
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público: accesible desde cualquier parte
        self.__saldo = saldo    # Atributo privado: el doble guion bajo (__) activa el name mangling

    def depositar(self, monto):
        # Método público que controla la modificación del atributo privado
        if monto > 0:
            self.__saldo += monto

    def ver_saldo(self):
        # Método getter público que permite consultar el saldo de forma segura
        return self.__saldo

# Instanciación y Pruebas

c = CuentaBancaria("Ana", 500)
c.depositar(200)

print(c.ver_saldo())  # Imprime: 700