"""
2. Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos 
números. 
"""
rango = int(input("Ingrese la cantidad de numeros que desea sumar:"))

suma = 0
for i in range(rango):
    numero = int(input("Ingrese numero:"))
    if numero < 0:
        numero *= -1
    suma += numero    
print("La suma de los numeros es: ",suma)        
