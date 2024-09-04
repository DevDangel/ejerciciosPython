"""
 Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un 
total de n personas.
"""
# Inicializamos las variables para contar cuántos hombres y mujeres hay
numHombres = 0
numMujeres = 0

# Pedimos al usuario el número total de personas en el salón
numPersonas = int(input("¿Cuántas personas hay en total en el salón? "))

# Verificamos que el número total de personas sea positivo
if numPersonas <= 0:
    print("El número total de personas debe ser mayor que cero. Inténtalo de nuevo.")
else:
    # Iteramos sobre el número total de personas para ingresar su género
    for i in range(numPersonas):
        # Pedimos al usuario que indique si la persona es hombre o mujer
        genero = input(f"Por favor, indica el género de la persona {i + 1} (hombre/mujer): ").strip().lower()

        # Contamos la persona según el género ingresado
        if genero == 'hombre':
            numHombres += 1
        elif genero == 'mujer':
            numMujeres += 1
        else:
            print("Entrada no válida. Por favor, ingresa 'hombre' o 'mujer'.")
            # No contamos ni sumamos si la entrada no es válida
            continue

    # Mostramos el total de hombres y mujeres en el salón
    print(f"Total de hombres en el salón: {numHombres}")
    print(f"Total de mujeres en el salón: {numMujeres}")
