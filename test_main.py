    
def leer_linea_por_linea(nombre_fichero):
    with open(nombre_fichero, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            yield linea.strip()



generador_lineas = leer_linea_por_linea("url.txt")
print(next(generador_lineas))  # Imprime la primera línea
print(next(generador_lineas))
