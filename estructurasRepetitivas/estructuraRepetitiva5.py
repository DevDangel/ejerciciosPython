# Definimos las categorías de edad
categorias = {
    "Niños": [],
    "Jóvenes": [],
    "Adultos": [],
    "Ancianos": []
}

# Recolectamos los datos de 50 personas
for i in range(50):
    print(f"\nPersona {i+1}")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso en kg: "))
    
    # Clasificamos a la persona en la categoría correspondiente
    if 0 <= edad <= 12:
        categorias["Niños"].append(peso)
    elif 13 <= edad <= 29:
        categorias["Jóvenes"].append(peso)
    elif 30 <= edad <= 59:
        categorias["Adultos"].append(peso)
    elif edad >= 60:
        categorias["Ancianos"].append(peso)
    else:
        print("Edad fuera de rango, por favor ingrese una edad válida.")

# Calculamos y mostramos el promedio de peso para cada categoría
for categoria, pesos in categorias.items():
    if len(pesos) > 0:
        promedio = sum(pesos) / len(pesos)
        print(f"\nEl promedio de peso en la categoría {categoria} es: {promedio:.2f} kg")
    else:
        print(f"\nNo se ingresaron datos para la categoría {categoria}.")