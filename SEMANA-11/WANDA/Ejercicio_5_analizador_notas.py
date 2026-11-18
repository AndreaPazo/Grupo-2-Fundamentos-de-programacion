import csv
import os

def analizar_notas(ruta):
    #calcula promedios,top alumnos y cantidad de aprobados
    alumnos = []
    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo) #csv.DictReader lee el archivo CSV y devuelve diccionario en file
        for fila in lector:
            notas = [float(fila["nota1"]), float(fila["nota2"]), float(fila["nota3"])]
            promedio = sum(notas) / len(notas)
            alumnos.append({"nombre": fila["nombre"], "promedio": promedio})

    for a in alumnos:
        print(f"{a['nombre']:<10} promedio: {a['promedio']:.2f}")

    top = max(alumnos, key=lambda a: a["promedio"]) #lambda función anónima que toma un argumento a 
    #devuelve a["promedio"]
    aprobados = len([a for a in alumnos if a["promedio"] >= 13])

    print(f"\nTop alumno: {top['nombre']} ({top['promedio']:.2f})")
    print(f"Aprobados (prom >= 13): {aprobados} de {len(alumnos)}")


if __name__ == "__main__": #__name__ var que indica si se ejecuta script
    carpeta_actual = os.path.dirname(os.path.abspath(__file__)) #os.path.dirname obtiene la ruta del directorio
    ruta_csv = os.path.join(carpeta_actual, "estudiantes.csv")
    analizar_notas(ruta_csv)
    #ejecuta en la terminal la ruta del CSV -- cd ...