"""
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa 
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio 
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos 
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad 
sea igual a 0.
"""
# Inicializamos los contadores y acumuladores para almacenar los datos
contadorHombres = 0          # Contador para la cantidad de hombres
contadorMujeres = 0          # Contador para la cantidad de mujeres
totalAltura = 0             # Acumulador para la suma de las alturas
contadorAlturaMayor170 = 0  # Contador para la cantidad de alumnos con altura mayor a 170 cm
contadorAlturaMenorIgual150 = 0  # Contador para la cantidad de alumnos con altura menor o igual a 150 cm
totalAlumnos = 0            # Contador para la cantidad total de alumnos
maxAlumnos = 5              # Limite de alumnos para el programa

# Bucle para ingresar los datos de los alumnos hasta alcanzar el límite
while totalAlumnos < maxAlumnos:
    # Pedimos el sexo del alumno y normalizamos la entrada a minúsculas
    sexo = input("Ingrese el sexo del alumno (hombre/mujer): ").strip().lower()

    # Pedimos la edad del alumno y manejamos el caso cuando la edad es 0
    while True:
        edad = int(input("Ingrese la edad del alumno: "))
        if edad == 0:
            print("Edad incorrecta. Por favor, ingrese una edad diferente de 0.")
        else:
            break  # Salimos del bucle cuando la edad es válida
    
    # Actualizamos los contadores de acuerdo al sexo del alumno
    if sexo == 'hombre':
        contadorHombres += 1
    elif sexo == 'mujer':
        contadorMujeres += 1
    else:
        print("Sexo no válido. Por favor, ingrese 'hombre' o 'mujer'.")
        continue  # Volvemos al inicio del bucle si el sexo no es válido
    
    # Pedimos la altura del alumno y la convertimos a float
    altura = float(input("Ingrese la altura del alumno en cm: "))

    # Acumulamos la altura y contamos el número total de alumnos
    totalAltura += altura
    totalAlumnos += 1

    # Actualizamos los contadores de altura basados en las condiciones
    if altura > 170:
        contadorAlturaMayor170 += 1
    if altura <= 150:
        contadorAlturaMenorIgual150 += 1

# Calculamos el promedio de altura solo si hay alumnos
if totalAlumnos > 0:
    promedioAltura = totalAltura / totalAlumnos
else:
    promedioAltura = 0  # Si no hay alumnos, el promedio de altura es 0

# Mostramos los resultados finales
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")
print(f"Altura promedio: {promedioAltura:.2f} cm")
print(f"Cantidad de alumnos con altura mayor a 170 cm: {contadorAlturaMayor170}")
print(f"Cantidad de alumnos con altura menor o igual a 150 cm: {contadorAlturaMenorIgual150}")


