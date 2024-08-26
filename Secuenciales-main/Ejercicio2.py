"""""
Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
del rectángulo es: yyyy
Nota: Se debe consultar la fórmula para hallar el perímetro y el área de un rectángulo.
"""
#Definimos variables de tipo numerico con decimal
base = float(input("Ingrese la base del rectangulo: "))#Pedimos que ingresen por consola la base del rectangulo
altura = float(input("Ingrese la altura del rectangulo: "))#Pedimos que ingresen por consola la altura del rectangulo
perimetro = float (2 * base + altura)#Definimos la variable que contiene la formula para hallar el perimetro (2 x base + altura)
area = float (base * altura)#Definimos la variable que contiene la formula para hallar el area (base x altura)
print(" El perimetro del rectangulo es: " ,perimetro ,'\n' ,"El area del rectangulo " ,area)

