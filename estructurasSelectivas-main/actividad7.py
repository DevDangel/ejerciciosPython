""""
En una llantera se ha establecido una promoción de las llantas marca "Todo Terreno", dicha promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10.
"""
#Titulos
print("***TIENDA DE LLANTAS MI CHILIN***")
print("Promocion en llantas marca \"todo terreno\"")
#Variables
compra = int(input("Ingrese la cantidad de llantas que desea comprar para conocer la promocion:"))
#Variables que contienen los precios segun la cantidad que ingrese
menosCinco = float(300000)
deCincoADiez = float(250000)
masDeDiez = float(200000)
#Estos mensajes se imprimiran si se cumplen las condicionales de abajo
mensaje1 = f"Por la compra de {compra} llanta(s), cada llanta tiene el valor de $300.000."#menos de 5
mensaje2 = f"Por la compra de {compra} llanta(s), cada llanta tiene el valor de $250.000."#de 5 a 10
mensaje3 = f"Por la compra de {compra} llanta(s), cada llanta tiene el valor de $200.000."#mas de 10
#condicionales anidadas que si se cumple la funcion le mostrara al usuario que por "x" cantidad de llantas que elijio la muestra el valor de la promocion
if compra < 5 and compra > 0:
    print(mensaje1)
elif compra >= 5 and compra <= 10:
    print(mensaje2)
elif compra > 10:
    print(mensaje3)
else:
    print("No es un numero de compra real")
           
#Operaciones de multiplicacion segun el numero que ingreso el usuario por el precio por cada llanta, (NOTA: se uso el metodo round por que la multiplicacion de numeros decimales se extiende.decimales)
compra1 = round(compra * menosCinco ,2)
compra2 = round(compra * deCincoADiez ,2)
compra3 = round(compra * masDeDiez ,2)
#Una vez que el usuario conozca la promoción se le pregunta si quiere realizar la compra para contabilizar la cantidad "x" por el valor de precio unitario por llanta
pregunta = input("Desea confirmar la compra?\n(SI/NO):").lower()#convierte cualquier cadena en minuscula
#Condicionales anidadas donde si se cumplen se realizan las operaciones de arriba y se manda a imprimir
if pregunta == "si" and compra < 5 and compra > 0:
    print("Muy bien, por la compra de",compra,"llanta(s) el valor a pagar es de",compra1)
elif pregunta == "si" and compra >= 5 and compra < 10:
    print("Muy bien, por la compra de",compra,"llanta(s) el valor a pagar es de",compra2)
elif pregunta == "si" and  compra > 10:
     print("Muy bien, por la compra de",compra,"llanta(s) el valor a pagar es de",compra3)
elif pregunta == "no":
    print("Entendido, espero te haya gustado la promocion y en un futuro estes aqui con nosotros para hacer la compra,\n muchas gracias por su atencion y lo esperamos de vuelta pronto.")
else:
    #Si el usuario ingresa algo diferente a "Si" y "No" se manda a imprimir este mensaje
    print("No confirmaste si deseas o no realizar la compra, igual que tengas un buen día")

                
