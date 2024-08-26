""""
Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.
Ejemplo: El vendedor Pepito Pérez, tiene un sueldo de xxxx, durante el mes obtuvo una comisión de
yyyy y el valor final a pagar es: zzzz
"""
#Definimos variables
nombreVendedor = input("Ingrese el nombre del vendedor: ")#Pedimos que ingresen por consola la literal de la variable del nombre del vendedor
sueldoBase = float(input("Ingrese su sueldo base: "))#Pedimos que ingresen por consola la literal de la variable del sueldo base
ventas = int(input("Ingrese el numero de ventas mensuales: "))#Pedimos que ingresen la literal de la variable de las ventas que realizo mensuales
comisionVenta = float(5000)#Definimos la variable de el valor de la comision por venta
sueldoMasComision = float(ventas * comisionVenta)#Hacemos la operacion para calcular la comision por el numero de ventas mensuales con la variable sueldoMasComision
sueldoTotal = sueldoBase + sueldoMasComision#Definimos la variable "SueldoTotal" realizando la suma del sueldo base mas la comision
#Mandamos a imprimir el mensaje concatenando las varaibles
print(" El vendedor " ,nombreVendedor ,", tiene un sueldo de " ,sueldoBase ," pesos " ,", durante el mes obtuvo una comision de " ,sueldoMasComision ," y el valor final a pagar es: " ,sueldoTotal)


 
