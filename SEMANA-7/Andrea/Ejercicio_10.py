# Dado un log de servidor web (formato Apache), extrae IP, método HTTP, 
# ruta y código de estado de cada línea usando solo métodos de strings

def server_log(log):
    partes = log.split()
    ip = partes[0]
    metodo_HTTP = partes[4].replace('"', '')
    ruta = partes[5]
    estado = partes[7]

    return ip, metodo_HTTP, ruta, estado

log = '192.168.1.10 - - [06/Oct/2026:10:30:15] "GET /index.html HTTP/1.1" 200 1234'

resultado = server_log(log)

print(resultado)