

# Dado un log de servidor web (formato Apache), extrae IP, método HTTP, ruta y código de estado de cada línea usando
# solo métodos de strings


def extraer_datos_log(linea):
    # Dividir la línea en partes usando espacios como separador
    partes = linea.split()

    # Extraer los datos relevantes
    ip = partes[0]  # La IP es la primera parte
    metodo_http = partes[5][1:]  # El método HTTP está entre comillas, se elimina la primera comilla
    ruta = partes[6]  # La ruta es la siguiente parte
    codigo_estado = partes[8]  # El código de estado es la novena parte

    return ip, metodo_http, ruta, codigo_estado

# Ejemplo de uso
log_linea = '192.168.1.1 - - [10/Oct/2023:13:55:20 +0000] "GET /index.html HTTP/1.1" 200 1234'
ip, metodo_http, ruta, codigo_estado = extraer_datos_log(log_linea)
print(f"IP: {ip}, Método: {metodo_http}, Ruta: {ruta}, Código de Estado: {codigo_estado}")

