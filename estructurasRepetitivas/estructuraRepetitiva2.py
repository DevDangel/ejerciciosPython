"""
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números.
"""

# Inicializa la variable suma en 0. Esta variable se utilizará para acumular la suma de los números convertidos a positivos.
suma = 0

# Los comentarios a continuación explican la fórmula utilizada para convertir un número negativo a positivo.
# Ejemplo:
# Si el número es -22, para convertirlo a positivo, se multiplica por -1.
# -22 * -1 = 22
#######################

# Imprime un mensaje para indicar el propósito del programa.
print("***CONVERTIR NUMEROS NEGATIVOS A POSITIVOS Y SUMARLOS***")

# Bucle que se repetirá 10 veces para leer 10 números.
for i in range(10):
    # Solicita al usuario que ingrese un número negativo y lo convierte a un entero.
    numero = int(input(f"Ingrese el {i+1}o número negativo:"))

    # Verifica si el número ingresado es negativo.
    if numero < 0:
        # Convierte el número negativo a positivo multiplicándolo por -1.
        numero = numero * -1
    
    # Suma el número convertido a positivo a la variable suma.
    suma += numero

# Imprime la suma total de los números convertidos a positivos.
print("La suma de los números convertidos es:", suma)
