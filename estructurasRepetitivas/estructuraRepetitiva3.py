""""
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja 
de todo el grupo.
"""
print("NOTAS PARA EL SALON 10B")
nota = float(input("Ingrese la 1ª nota:"))
calificacionAlta = nota
calificacionBaja = nota
suma = nota

for i in range(20):
    nota = float(input(f"Ingre la {i+2}ª nota:"))
    suma += nota
    if nota > calificacionAlta:
        calificacionAlta = nota
    if nota < calificacionBaja:
        calificacionBaja = nota
    promedio = round(suma / 20,2)
print("El promedio de nota por el grupo es:",promedio) 
print("La calificacion mas alta es:",calificacionAlta)   
print("La calificacion mas baja es:",calificacionBaja)