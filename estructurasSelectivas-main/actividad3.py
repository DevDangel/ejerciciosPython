"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante://

-Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, 
pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.//

-Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. 
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito solicitado al fabricante, según sea el caso.//
"""
""""""""
import sys #Importamos el modulo sys para interactuar con variables
#Titulos
print("***TIENDA DE BOLSOS ESCOBAR Y URIBE***")
producto = input("Que articulo desea comprar\n(bolsos/ maletas / carrieles / canguros)\n").lower()
#Precio de los productos
bolsosPrecio = float(60000)
maletasPrecio = float(120000)
carrielesPrecio = float(50000)
cangurosPrecio = float(20000)

#Estas condicionales anidadas son para que la variable "producto" cuando reciba cadenas similares, pase a ser la variable que contiene el valor de cada articulo
if producto == "bolsos":
    producto = bolsosPrecio
elif producto == "maletas":
    producto = maletasPrecio
elif producto == "carrieles":
    producto = carrielesPrecio
elif producto == "canguros":
    producto = cangurosPrecio
else:
    print("Ese producto no lo tenemos en nuestra tienda")
    sys.exit()#Usamos la funcion en python sys con el exit() para detener la ejecucion del programa si se cumple la ultima condicional    

#Pedimos que ingrese la cantidad de articulos que va a comprar
cantidad = int(input("Ingrese la cantidad de articulos que desea comprar:"))
#Definimos la variable que contiene la cantidad de articulos por el precio
montoTotal = cantidad * producto
#Definimos los porcentajes
#primera condicional con la funcion round 2 para redondear numeros decimales
inversionUno = round(0.55 * montoTotal, 2) #55% de inversion
prestamoBanco = round(0.30 * montoTotal, 2)#30% de prestamo bancario
pagoCreditoUno = round(0.70 * montoTotal, 2)#El resto lo pagara a credito al fabricante osea un 70%
#Segunda Condicional
inversionDos = round(0.70 * montoTotal, 2)#70% de inversion
pagoCreditoDos = round(0.30 * montoTotal, 2)#30% lo pagara a credito al fabricante
cobroIntereses = round(pagoCreditoDos * 0.20, 2)#el fabricante cobra 20% de interes sobre la cantidad que se le pague a credito

#Condicionales duales
#Y mandamos a imprimir el resultado final
if (montoTotal < 500000) and (montoTotal > 0):
    print("La compra fue realizada con exito con un total de" ,montoTotal ,"pesos,","el valor de la inversion que hará la empresa es de" ,inversionDos ,"pesos,",'\n',"el dinero restante que se pagará a credito al fabricante es de" ,pagoCreditoDos ,"pesos," ,"el fabricante por concepto de interes cobrará" ,cobroIntereses ,"pesos de interes.")
else:
    print("La compra fue realizada con exito con un total de" ,montoTotal ,"pesos,","el valor de la inversion que hará la empresa es de" ,inversionUno ,"pesos,",'\n',"se pide prestado al banco la suma de" ,prestamoBanco ,"pesos," ,"y la deuda a credito con el fabricante queda en el valor de" ,pagoCreditoUno ,"pesos.")
