class Temperatura:
    def __init__(self, celsius=0):
        # Asigna el valor inicial a través del atributo protegido _celsius
        self._celsius = celsius

    @property
    def celsius(self):
        # GETTER: Permite leer el valor como si fuera un atributo público (t.celsius)
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        # SETTER: Intercepta la asignación (t.celsius = valor) para aplicar validaciones de dominio
        if valor < -273.15:
            raise ValueError("Bajo cero absoluto")  # Impide valores físicamente imposibles
        self._celsius = valor

# Instanciación y Pruebas

t = Temperatura()   # Se inicializa con valor por defecto celsius = 0
t.celsius = 25      # Invoca internamente al método @celsius.setter (pasa la validación)

print(t.celsius)    # Invoca internamente al método @property (getter). Imprime: 25