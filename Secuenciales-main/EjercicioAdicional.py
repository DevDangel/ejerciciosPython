""""
Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las
siguientes apreciaciones:
• Actividades en clase equivalen a un porcentaje de 30%
• Proyecto final 50%
• Evaluaciones parciales 20%
Para esto es importante definir 4 variables.
Variable 1 que almacene el nombre del estudiante
Variable 2 que almacene la calificación promedio de las actividades realizadas en clase
Variable 3 que almacene la calificación del proyecto final
Variable 4 que almacene la calificación promedio de las evaluaciones parciales
Se debe calcular la calificación final.
El algoritmo debe mostrar el nombre del estudiante, junto con la nota final del estudiante.
Ejemplo: La nota final de algoritmia del estudiante xxxx es: yyyy
"""
# Definir las variables
nombreEstudiante = input("Ingrese el nombre del estudiante: ")#Pedimos por consola que ingrese la literal de la variable
calificacionActividades = float(input("Ingrese la calificación promedio de las actividades en clase (0-100): "))#Pedimos por consola que ingrese la literal de la variable
calificacionProyecto = float(input("Ingrese la calificación del proyecto final (0-100): "))#Pedimos por consola que ingrese la literal de la variable
calificacionEvaluaciones = float(input("Ingrese la calificación promedio de las evaluaciones parciales (0-100): "))#Pedimos por consola que ingrese la literal de la variable

# Definir los porcentajes
porcentajeActividades = 0.30
porcentajeProyecto = 0.50
porcentajeEvaluaciones = 0.20

# Calcular la nota final
nota_final = (calificacionActividades * porcentajeActividades +
              calificacionProyecto * porcentajeProyecto +
              calificacionEvaluaciones * porcentajeEvaluaciones)

#Imprimimos el resultado
print("La nota final de algoritmia del estudiante", nombreEstudiante, "es:", round(nota_final, 2)) #funcion "round " para redondear un numero decimal largo
 