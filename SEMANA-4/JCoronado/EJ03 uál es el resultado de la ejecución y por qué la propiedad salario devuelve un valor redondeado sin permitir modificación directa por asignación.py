class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre        # Atributo público
        self.__salario = salario    # Atributo privado con name mangling

    def aumentar_salario(self, pct):
        # Método público que aplica el porcentaje de aumento sobre el atributo privado
        self.__salario *= (1 + pct / 100)

    @property
    def salario(self):
        # GETTER: Retorna el salario de solo lectura redondeado a 2 decimales
        return round(self.__salario, 2)
# Instanciación y Pruebas
e = Empleado("Carlos", 3000)
e.aumentar_salario(10)
print(e.salario)  # Imprime: 3300.0