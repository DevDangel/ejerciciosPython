"""
Calcular el total a pagar por la compra de zapatillas. 
Si se compran tres o más zapatillas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. 
Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento.
"""
#titulo
print("***TIENDA DE ZAPATILLAS NIKE***")
print("Zapatillas con el 10% de descuento")
print("o por la compra de 3 o mas Zapatillas adquiere un 20% de descuento")
#Definimos variables tanto cantidad por total
cantidad = int(input("Buen dia ingrese la cantidad de zapatillas que desea comprar:"))
totalZap = float(input("Ingrese el toltal del valor de la compra de las zapatillas:"))
#Variables que almacenan el descuento
#20%
veintePorCiento = float(totalZap * 0.20)
#formula para sacarle el 20% a un valor
compraConVeintePorCiento = (totalZap - veintePorCiento)
#10% 
diezPorCiento = float(totalZap * 0.10)
#formula para sacarle el 10% a un valor 
compraConDiezPorCiento = (totalZap - diezPorCiento) 
#condicionales
if cantidad >= 3:
    print("Por la compra de" ,cantidad ,"zapatillas, con un valor total de" ,totalZap ,"mas un descuento del 20% el valor a pagar de la compra es de" ,compraConVeintePorCiento)
else:
     print("Por la compra de" ,cantidad ,"zapatillas, con un valor total de" ,totalZap ,"mas un descuento del 10% el valor a pagar de la compra es de" ,compraConDiezPorCiento)
