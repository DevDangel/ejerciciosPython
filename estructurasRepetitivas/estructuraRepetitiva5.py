"""
 Una persona debe realizar un muestreo con 50 personas para determinar el 
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 
Las categorías se determinar de acuerdo a la siguiente tabla:
CATEGORIA          EDAD
Niños              0 - 12 
Jovenes            13 - 29
Adultos            30 - 59
Ancianos           60 en adentante
"""
# Variables para contar el número de personas en cada grupo de edad
numNinos = 0
numJovenes = 0
numAdultos = 0
numAncianos = 0

# Variables para acumular el peso total de cada grupo de edad
pesoTotalNinos = 0
pesoTotalJovenes = 0
pesoTotalAdultos = 0
pesoTotalAncianos = 0

# Realizar el muestreo de 50 personas
for i in range(50):
    # Pedir al usuario que ingrese la edad y el peso de la persona
    edad = int(input("Por favor, ingrese la edad de la persona: "))
    peso = float(input("Ahora, ingrese el peso de la persona (en kg): "))

    # Determinar a qué grupo de edad pertenece la persona y acumular el peso
    if 0 <= edad <= 12:
        numNinos += 1
        pesoTotalNinos += peso
    elif 13 <= edad <= 29:
        numJovenes += 1
        pesoTotalJovenes += peso
    elif 30 <= edad <= 59:
        numAdultos += 1
        pesoTotalAdultos += peso
    elif edad >= 60:
        numAncianos += 1
        pesoTotalAncianos += peso
    else:
        print("La edad ingresada no es válida. Por favor, intente de nuevo.")
        # Si la edad es inválida, no se cuenta ni se acumula el peso
        continue

# Calcular y mostrar el promedio de peso para cada grupo de edad
if numNinos > 0:
    promedioPesoNinos = pesoTotalNinos / numNinos
    print(f"El promedio de peso de los niños es: {promedioPesoNinos:.2f} kg")
else:
    print("No se ingresaron datos para los niños.")

if numJovenes > 0:
    promedioPesoJovenes = pesoTotalJovenes / numJovenes
    print(f"El promedio de peso de los jóvenes es: {promedioPesoJovenes:.2f} kg")
else:
    print("No se ingresaron datos para los jóvenes.")

if numAdultos > 0:
    promedioPesoAdultos = pesoTotalAdultos / numAdultos
    print(f"El promedio de peso de los adultos es: {promedioPesoAdultos:.2f} kg")
else:
    print("No se ingresaron datos para los adultos.")

if numAncianos > 0:
    promedioPesoAncianos = pesoTotalAncianos / numAncianos
    print(f"El promedio de peso de los ancianos es: {promedioPesoAncianos:.2f} kg")
else:
    print("No se ingresaron datos para los ancianos.")
