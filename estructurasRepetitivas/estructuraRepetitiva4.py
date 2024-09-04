"""
Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
"""
# Imprimir el título del programa
print("TABLA DE MULTIPLICAR")

# Solicitar al usuario que ingrese un número para conocer su tabla de multiplicar
numero = int(input("Ingrese el numero que desea conocer su tabla de multiplicar:"))

# Iterar desde 1 hasta 10 para generar la tabla de multiplicar
for i in range(1, 11):
    # Calcular el producto del número ingresado y el valor actual de i
    multiplicar = numero * i
    # Imprimir el resultado en el formato: número x i = resultado
    print(f"{numero} x {i} = {multiplicar}")

