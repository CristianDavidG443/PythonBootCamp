"""Escribir un programa que permita leer la edad y peso de una persona y 
posteriormente imprimirla."""

"""
# Pedir la edad
edad = input("Ingresa tu edad: ")

# Pedir el peso
peso = input("Ingresa tu peso en kilogramos: ")

# Mostrar los datos
print("Tienes", edad, "años y pesas", peso, "kg.")
"""
"""Escribir un programa que calcule el área de un triángulo recibiendo como 
entrada el valor de base y altura. Área= base*altura/2 """

"""""
# Solicitar la base del triángulo
base = float(input("Ingresa la base del triángulo: "))

# Solicitar la altura del triángulo
altura = float(input("Ingresa la altura del triángulo: "))

# Calcular el área utilizando la fórmula
area = (base * altura) / 2

# Mostrar el resultado
print("El área del triángulo es:", area)
"""
"""Escribir un programa que calcule el área de un círculo.  
Area= radio*radio*Pi """""

"""""
import math  # Importamos el módulo 'math' para usar el valor de pi

# Solicitar el radio del círculo al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área
area = math.pi * radio ** 2  # '** 2' significa 'elevado al cuadrado'

# Mostrar el resultado
print("El área del círculo es:", area)
"""
"""Hacer un programa que permita ingresar el peso de una persona en kilogramos y 
devolver dicho peso en libras."""

""""
# Solicitar el peso en kilogramos
kg = float(input("Ingresa tu peso en kilogramos: "))

# Convertir a libras
libras = kg * 2.20462

# Mostrar el resultado
print("Tu peso en libras es:", libras)
"""
"""En un supermercado de la ciudad se está aplicando un descuento del 10% sobre 
las compras que hacen los clientes. Diseñar un programa que calcule y escriba el 
descuento en pesos que se hace sobre la compra y el valor total que deberá pagar 
el cliente."""
"""""
# Compra sin descuento 
compra =float(input("Precio de la compra"))

#10% de descuento
descuento = compra * 0.10

#Total a pagar luego del descuento
total=compra-descuento

#Mostrar los resultados
print("Descuento aplicado: $" , round(descuento, 2))
print("total a pagar: $", round(total, 2))
"""
"""Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en 
cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera 
al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la 
nota definitiva del estudiante."""

""""
#notas

nota1=float(input("ingrese su nota 1:"))
nota2=float(input("Ingrese su nota 2:"))
nota3=float(input("ingrese su nota 3:"))
nota4=float(input("ingrese su nota 4:"))

#nota definitiva

definitiva = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)

#Resultado nota final
print("la nota definitiva del estudiante es:", round(definitiva, 2))
"""
"""Construya un programa tal que dados los datos enteros A y B, escriba el resultado 
de la siguiente expresión: 
(A + B)2 
3 """
"""
 # Solicitar los datos enteros A y B
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))

# Calcular la expresión: (A + B)² / 3
resultado = ((A + B) ** 2) / 3

# Mostrar el resultado
print("El resultado de la expresión es:", resultado)
"""
"""Diseñe un programa que calcule e imprima el número de segundos que hay en un 
determinado número de días."""

"""""
# Solicitar la cantidad de días
dias = int(input("Ingresa el número de días: "))

# Calcular los segundos
segundos = dias * 24 * 60 * 60

# Mostrar el resultado
print("El número de segundos en", dias, "día(s) es:", segundos)
"""
""" Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su 
suma y su promedio."""
"""
# Solicitar los cuatro valores al usuario
valor1 = float(input("Ingresa el primer valor: "))
valor2 = float(input("Ingresa el segundo valor: "))
valor3 = float(input("Ingresa el tercer valor: "))
valor4 = float(input("Ingresa el cuarto valor: "))

# Calcular la suma
suma = valor1 + valor2 + valor3 + valor4

# Calcular el producto
producto = valor1 * valor2 * valor3 * valor4

# Calcular el promedio
promedio = suma / 4

# Mostrar los resultados
print("La suma de los valores es:", suma)
print("El producto de los valores es:", producto)
print("El promedio de los valores es:", round(promedio, 2))
 """

"""
Diseñar un programa que permita calcular e imprimir el salario neto de un 
trabajador conociendo el número de horas trabajadas y el precio de la hora, y 
teniendo en cuenta que se le va a descontar el 8% de lo que se gana.
""" 

#1) Determinar si un número entero dado por el usuario es par o impar
"""
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print("El numero", numero, "es par.")   
else:
    print("El numero", numero, "es impar")
"""
#2) Determinar si un número entero dado por el usuario es positivo o negativo       
""""
numero = int(input("Ingresa un numero entero: "))
if numero >= 0:
    print("El numero", numero, "es positivo.")
else:
    print("El numero", numero, "es negativo.")
"""  
#3) Determinar en qué estado está el agua en función de su temperatura. Si es negativa el
#estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será
#gas. Pedir al usuario el valor de la temperatura.
"""
valor = float(input("Ingresa la temperatura del agua en grados Celsius: "))
if valor < 0:
    print("El agua está en estado sólido.")
elif valor < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.")
"""
#4) Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
#divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.

"""
año = int(input("Ingresa un Año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es bisiesto.")
else:
    print("El año", año, "no es bisiesto.")
"""
#5) Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo
#trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora.
#El cálculo se realiza del siguiente modo:
#• Las primeras 35 horas se pagan a la tarifa normal.
#• Las horas extras se pagan un 25% más que las normales.
#• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
#• Si el sueldo es menor de 1000€, libre de impuestos.
#• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
#• Si el sueldo es mayor de 2000€, el 30%.


numero_horas = float(input("Ingrese el numero de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio de la hora trabajada: "))
if numero_horas <=35:
    totalsemanales = numero_horas * precio_hora
else:
    precio_hora_extra = precio_hora * 1.25
    horas_extras = numero_horas - 35
    totalsemanales = (35 * precio_hora) + (horas_extras * precio_hora_extra)
salario_mensual = totalsemanales * 4  # Asumiendo 4 semanas en un mes
if salario_mensual < 1000:
    impuestos = 0
elif 1000 <= salario_mensual < 2000:
    impuestos = salario_mensual * 0.20
elif salario_mensual >= 2000:
    impuestos = salario_mensual * 0.30

# Calcular el salario bruto
salario_neto = numero_horas * precio_hora
print("el salario neto es: $", round(salario_neto,2))



