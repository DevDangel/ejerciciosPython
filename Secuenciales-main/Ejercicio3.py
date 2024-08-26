"""""
Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los
números ingresado es: xxxx
"""
#Promedio de tres numeros ingresados
print("Promedio de tres numeros")#Iniciamos el algoritmo con un titulo 
#Definimos variables
numero1 = int(input("Ingrese el primer numero:"))#Pedimos que ingresen por consola el primer numero que se almacena en la variable numero1
numero2 = int(input("Ingrese el segundo numero:"))#Pedimos que ingresen por consola el segundo numero que se almacena en la variable numero2
numero3 = int(input("Ingrese el tercer numero:"))#Pedimos que ingresen por consola el tercernumero que se almacena en la variable numero1
suma = int(numero1 + numero2 + numero3 )#Hacemos la variable "suma" donde sume los tres numeros ingresados
promedio = int(suma / 3)#La variable "promedio" donde hace la operacion de la suma divido en 3
print("El promedio de los numeros es:" ,promedio)#Imprimos el promedio