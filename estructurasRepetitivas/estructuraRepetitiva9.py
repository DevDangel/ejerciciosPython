"""
Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos. 
"""
# Inicializamos las variables para contar y sumar las edades
totalEdadHombres = 0  # Total de edades de los hombres
totalEdadMujeres = 0  # Total de edades de las mujeres
totalEdadAlumnos = 0  # Total de edades de todos los alumnos

contadorHombres = 0  # Contador de hombres
contadorMujeres = 0  # Contador de mujeres
contadorAlumnos = 0  # Contador de alumnos en total

# Pedimos al usuario el número total de alumnos
numAlumnos = int(input("¿Cuántos alumnos hay en el grupo? "))

# Verificamos que el número total de alumnos sea positivo
if numAlumnos <= 0:
    print("El número total de alumnos debe ser mayor que cero. Inténtalo de nuevo.")
else:
    # Usamos un bucle para ingresar los datos de cada alumno
    for i in range(numAlumnos):
        # Pedimos el género del alumno
        genero = input(f"Ingrese el género del alumno {i + 1} (hombre/mujer): ").strip().lower()
        
        # Verificamos que el género ingresado sea válido usando condiciones or
        if genero != 'hombre' and genero != 'mujer':
            print("Género no válido. Por favor, ingresa 'hombre' o 'mujer'.")
            continue  # Si el género no es válido, pedimos el siguiente alumno

        # Pedimos la edad del alumno
        edad = int(input(f"Ingrese la edad del alumno {i + 1}: "))
        
        # Sumamos la edad al total y contamos el número de alumnos
        totalEdadAlumnos += edad
        contadorAlumnos += 1
        
        # Sumamos la edad al total de la categoría correspondiente
        if genero == 'hombre':
            totalEdadHombres += edad
            contadorHombres += 1
        elif genero == 'mujer':
            totalEdadMujeres += edad
            contadorMujeres += 1

    # Calculamos los promedios usando estructuras if convencionales
    if contadorHombres > 0:
        promedioEdadHombres = int(totalEdadHombres / contadorHombres)
    else:
        promedioEdadHombres = 0  # Si no hay hombres, el promedio es 0

    if contadorMujeres > 0:
        promedioEdadMujeres = int(totalEdadMujeres / contadorMujeres)
    else:
        promedioEdadMujeres = 0  # Si no hay mujeres, el promedio es 0

    if contadorAlumnos > 0:
        promedioEdadAlumnos = int(totalEdadAlumnos / contadorAlumnos)
    else:
        promedioEdadAlumnos = 0  # Si no hay alumnos, el promedio es 0

    # Mostramos los resultados #Formateando con int para que no salga punto decimal
    print(f"Promedio de edad de los hombres: {int(promedioEdadHombres)} años")
    print(f"Promedio de edad de las mujeres: {int(promedioEdadMujeres)} años")
    print(f"Promedio de edad de todos los alumnos: {int(promedioEdadAlumnos)} años")
