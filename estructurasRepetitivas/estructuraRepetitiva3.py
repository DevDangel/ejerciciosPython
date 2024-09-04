""""
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja 
de todo el grupo. 
"""
# Solicitar al usuario la cantidad de notas que se ingresarán
cuantas = int(input("Ingrese la cantidad de notas que tiene en el grupo:"))

# Solicitar la primera nota e inicializar las variables con ella
notas = float(input("Ingrese la 1ª nota:"))

# Inicializar las variables para la calificación más alta, más baja y la suma de las notas
calificacionAlta = notas
calificacionBaja = notas
suma = notas

# Iterar desde 1 hasta la cantidad de notas menos 1 (ya que la primera nota ya fue ingresada)
for i in range(1, cuantas):
    # Solicitar al usuario la siguiente nota
    notas = float(input(f"Ingrese la {i+1}ª nota:"))
    
    # Acumular la nota en la variable suma
    suma += notas
    
    # Actualizar la calificación más alta si la nota actual es mayor
    if notas > calificacionAlta:
        calificacionAlta = notas
    
    # Actualizar la calificación más baja si la nota actual es menor
    if notas < calificacionBaja:
        calificacionBaja = notas

# Calcular el promedio de las notas, redondeado a dos decimales
promedio = round(suma / cuantas, 2)

# Imprimir el promedio, la calificación más alta y la calificación más baja
print("El promedio de las notas de todo el grupo es:",promedio,"\n La calificacion mas alta es: ",calificacionAlta,"\n la calificacion mas baja es: ",calificacionBaja)            