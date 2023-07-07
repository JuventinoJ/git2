def contar_palabras(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print("El archivo no existe.")
        return 0

nombre_archivo = input("Ingresa el nombre del archivo: ")

cantidad_palabras = contar_palabras(nombre_archivo)
print("El archivo contiene", cantidad_palabras, "palabras.")
