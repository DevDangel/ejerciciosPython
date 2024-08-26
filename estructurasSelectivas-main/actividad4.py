"""
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar. 
Si el color de la balota es rojo el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si el color es diferente a los indicados no obtendrá descuento. 
Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar.
"""
import sys
#Importamos el modulo random para poder ser mas interactivos y generar una boleta al azar
import random
#Titulos
print("***SUPERMERCADO WEEKS***")
#Variable que contiene el total de la compra
totalCompra = float(input("Ingrese el total de la compra y participe en la promocion de descuentos:"))
#Titulos
print("***PROMOCION BOLETAS DE DESCUENTO***\n(rojo / verde / azul / amarilla)\nporfavor presione \"1 para escoger al azar una boleta: ")
alAzar = input()
#Variables con formulas matematicas para sacar porcentajes quitar 15%
boletaRoja = totalCompra - (0.15 * totalCompra)#15%
boletaVerde = totalCompra - (0.20 * totalCompra)#20%
#mensajes cuando la boleta no contiene el descuento
boletaAzul = "boleta azul, no aplica descuento, puede seguir participando en otro momento"
boletaAmarilla = "boleta amarilla no aplica descuento, puede seguir participando en otro momento"
#variable que contiene los colores de las boletas
colores = ["rojo", "verde", "azul", "amarillo"]
#condicional simple utilizando la funcion random.choice para elejir al azar un (color)
if alAzar != "1":
    print("Parece que no quieres participar")
    sys.exit()
elif alAzar == "1":
    boletaElegida = random.choice(colores)
    #Imprimimos primer mensaje
    print("El valor de la compra fue" ,totalCompra ,"el color de su boleta es",boletaElegida)
    
#Condicional anidada para tranformar la variable "boletaElegida" en las variables que contienen la formula del porcentaje o los mensajes    
if boletaElegida == "rojo":
    #Imprimimos el segundo mensaje si se cumple la condicion
    print("usted obtiene un descuento del 15% con un valor a pagar de",boletaRoja ,"gracias por participar vuelve pronto.")
elif boletaElegida == "verde":
    #Imprimimos el segundo mensaje si se cumple la condicion
    print("usted obtiene un descuento del 20% con un valor a pagar de" ,boletaVerde ,"gracias por participar vuelve pronto")
elif boletaElegida == "azul":
    #Imprimimos el segundo mensaje si se cumple la condicion
    print(boletaAzul)
elif boletaElegida == "amarillo":
    #Imprimimos el segundo mensaje si se cumple la condicion
    print(boletaAmarilla)
else:
    #sys.exit para finalizar el programa por si ocurre algo que no tenga que ver con las boletas
    sys.exit()
