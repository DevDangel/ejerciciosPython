"""
Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, 
se le hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno.
"""
#Titulos
print("***SER PILO PAGA***")
print("Si su promedio es 4.0 o más, obtienes el 30% de descuento en la pension")
#Definimos variables
nombre = input("Ingrese el nombre del alumno\n") 
pension = float(input("Ingrese el valor de su pensión:\n"))
nota1 = float(input("Ingrese su primera nota(0 - 5.0):\n"))
nota2 = float(input("Ingrese su segunda nota(0 - 5.0):\n"))
nota3 = float(input("Ingrese su tercera nota(0 - 5.0):\n"))
nota4 = float(input("Ingrese su cuarta nota(0 - 5.0):\n"))
nota5 = float(input("Ingrese su quinta nota(0 - 5.0):\n"))
#Variable que contiene la formula de promedio
promedio =(nota1 + nota2 + nota3 + nota4 + nota5)/5
resultado = round(promedio ,2)#redondeamos el promedio para que no se exceda en decimales
#Descuento del -30%
treintaPorCiento = (0.30 * pension)
#Mas IVA 10%
iva = (pension)+(0.10 * pension)
#Condicionales
if promedio >= 4.0 and promedio <= 5.0:
    print("El promedio obtenido en el ultimo periodo es de:",resultado ,"por lo tanto cumple con los requisitos para el descuento de 30%\npor lo que el alumno",nombre,"debera pagar en pensión:",treintaPorCiento,"pesos")
elif promedio >= 0 and promedio < 4.0:
    print("El alumno",nombre,"obtuvo un promedio de:",resultado,"esto es por debajo del requisito del 30%\npor lo que debera pagar la pensión completa mas un 10% IVA. Total a pagar:",iva)
else:
    print("Ocurrio un error inesperado, revise si las notas que ingrenso se encuentran de(0 - 5.0)") 
