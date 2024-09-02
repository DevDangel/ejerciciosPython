""""
Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
"""
print("TABLA DE MULTIPLICAR")
numero = int(input("Ingrese el numero que desea conocer su tabla de multiplicar:"))
for i in range(1,11):
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")