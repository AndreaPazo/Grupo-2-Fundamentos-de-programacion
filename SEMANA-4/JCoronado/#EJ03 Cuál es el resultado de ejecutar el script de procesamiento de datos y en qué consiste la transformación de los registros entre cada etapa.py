def leer_datos(fuente):
    # Simula la lectura de un archivo y retorna una lista de números enteros
    return [1, -2, 3, -4, 5]

def filtrar_positivos(datos):
    # LISTA POR COMPRENSIÓN: Filtra la lista reteniendo únicamente los valores mayores a 0
    return [x for x in datos if x > 0]

def calcular_estadisticas(datos):
    # Retorna un diccionario con métricas clave aplicadas sobre los datos limpios
    return {
        "suma": sum(datos),
        "media": sum(datos) / len(datos),
        "max": max(datos)
    }

# PIPELINE MODULAR (Flujo de datos)
# Etapa 1: Ingesta de datos
datos = leer_datos("archivo.csv")  # Resultado: [1, -2, 3, -4, 5]

# Etapa 2: Limpieza y filtrado
limpios = filtrar_positivos(datos)  # Resultado: [1, 3, 5]

# Etapa 3: Procesamiento y agregación
stats = calcular_estadisticas(limpios)

print(stats)  # Imprime: {'suma': 9, 'media': 3.0, 'max': 5}