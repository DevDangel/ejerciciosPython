""""
Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros.
"""
positivo = 0
negativo = 0
neutro = 0

# Bucle para leer 5 números ingresados por el usuario
for i in range(5):
    # Solicita al usuario que ingrese un número y lo convierte a entero
    numero = int(input(f"Ingrese los numeros {i+1}:"))
    
    # Verifica si el número es positivo, negativo o neutro (cero)
    if numero > 0:
        positivo +=1  # Incrementa el contador de positivos si el número es mayor a 0
    elif numero < 0:
        negativo += 1  # Incrementa el contador de negativos si el número es menor a 0
    else:
        neutro +=1  # Incrementa el contador de neutros si el número es igual a 0

# Imprime la cantidad total de números positivos, negativos y neutros ingresados
print("Cantidad de numeros postivos:", positivo)
print("Cantidad de numeros negativos:", negativo)
print("Cantidad de numeros neutros:", neutro)
    