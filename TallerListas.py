
#Calcular el producto de todos los elementos de una lista de n posiciones.
"""""
def producto_lista(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto 
# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = producto_lista(lista)
print(f"El producto de los elementos de la lista {lista} es: {resultado}")
"""
Calcular la suma de todos los elementos de una lista de n posiciones.
def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = suma_lista(lista)
print(f"La suma de los elementos de la lista {lista} es: {resultado}")

