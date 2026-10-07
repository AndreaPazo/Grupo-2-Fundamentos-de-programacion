# Cadena multilínea que simula registros en formato CSV
datos_csv = """Juan Perez,18,Arequipa
Maria Lopez,15,Lima
Carlos Gomez,20,Trujillo"""

# Separa el texto por saltos de línea para obtener cada fila usando .splitlines()
filas = datos_csv.splitlines()

# Imprime la cabecera formateada de la tabla
print(f"{'NOMBRE':<15} | {'NOTA':<5} | {'CIUDAD':<10}")
print("-" * 37)

# Iteración sobre cada fila de datos
for fila in filas:
    # Divide la fila en campos usando la coma como separador mediante .split(',')
    nombre, nota, ciudad = fila.split(",")
    
    # Limpia posibles espacios en blanco restantes en cada campo usando .strip()
    nombre = nombre.strip()
    nota = nota.strip()
    ciudad = ciudad.strip()
    
    # Muestra los datos alineados en formato de columnas
    print(f"{nombre:<15} | {nota:<5} | {ciudad:<10}")