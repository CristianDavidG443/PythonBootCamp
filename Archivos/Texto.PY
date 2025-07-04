archivo = open("texto.txt", "w")
archivo.write("Hola, mundo!\n")
archivo.write("Este es un archivo de texto.\n")

for i in range(1, 6):
    archivo.write(f"Linea {i}\n")

archivo.close()
# Cerrar el archivo

archivo = open("texto.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Cerrar el archivo después de leer
for linea in contenido.split('\n'):
    línea = linea.strip()  # Eliminar espacios en blanco al inicio y al final :
    print(línea)