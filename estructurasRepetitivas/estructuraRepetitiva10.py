"""
Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
(1*2*3*4*5…)
"""
# Inicializamos la variable para almacenar el resultado de la multiplicación
resultado = 1

# Imprimimos los cálculos paso a paso
for i in range(1, 21):
    if i == 1:
        # Inicializamos con un encabezado
        print("Multiplicacion numeros naturales:")
    else:
        # Imprimimos el cálculo actual
        print(f"{resultado} × {i} = {resultado * i}")
    
    # Actualizamos el resultado de la multiplicación
    resultado = resultado * i
