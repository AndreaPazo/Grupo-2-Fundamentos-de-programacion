# Función 1: Procesa la lista recibida por referencia y retorna 3 valores
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    nota_minima = min(notas)
    nota_maxima = max(notas)
    # Múltiples retornos: Python empaqueta estos valores en una tupla
    return promedio, nota_minima, nota_maxima

# Función 2: Función void que genera e imprime el reporte formateado
def mostrar_resultado(nombre, notas):
    # Desempaquetado del retorno múltiple de la función calcular_promedio
    prom, mn, mx = calcular_promedio(notas)
    
    # Reporte en pantalla
    print(f"=== REPORTE DE NOTAS: {nombre.upper()} ===")
    print(f"Notas registradas: {notas}")
    print(f"Promedio: {prom:.2f}")
    print(f"Nota más baja: {mn}")
    print(f"Nota más alta: {mx}")
    print("=" * 35)

# --- PRUEBA Y EJECUCIÓN DEL EJERCICIO 3 ---
estudiante = "Carlos"
lista_de_notas = [14, 18, 11, 20, 15]

# Llamamos a la función principal para generar el reporte
mostrar_resultado(estudiante, lista_de_notas)