""""
Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.
"""
#Titulo del algoritmo
print("CALIFICACION FINAL ALGORITMIA")
#definimos variables mediante consola (metodo input)
nombre = input("Ingrese el nombre del estudiante:")
nota1 = float(input("Ingrese la primera nota:(0 - 100)"))
nota2 = float(input("Ingrese la segunda nota:(0 - 100)"))
nota3 = float(input("Ingrese la tercera nota:(0 - 100)"))
#variables de formulas matematicas para hallar el promedio
suma = float(nota1 + nota2 + nota3)
promedio = (suma)/3
#Condicional para saber si el estudiante aprobo
#Si la nota promedio es mayor o igual que 70 entonces se imprime el mensaje
if promedio >= 70 and promedio < 100:
    #mensaje
    print("El estudiante" ,nombre ,"aprobo Algoritmia")
#Se corrobora que la nota promedio no supere los 100 o arroja error   
elif promedio >= 101:
    print("Ingreso una nota demasiada alta, error en promedio")
#Si no cumple las dos condiciones entonces se cumple la ultima (promedio < 70)    
else:
     print("El estudiante" ,nombre ,"no aprobo Algoritmia")
          
