"""
Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica es:
.cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10
.y si el sexo es masculino: núm. pulsaciones = (210 - edad)/10
"""
#Titulos
print("CALCULAR NUMEROS DE PULSACIONES")
#Definimos variables
nombre = input("Ingrese por favor su nombre:")
edad = int(input("Ingrese por favor su edad:"))
genero = input("Ingrese por favor su sexo/genero \n (Masculino / Femenino)\n").lower()#Tranformar en minuscula cualquier valor


#Formulas
numPulsacionesHombres = (210 - edad)/10
numPulsacionesMujeres = (220 - edad)/10

#Condicionales anidada
if genero == "masculino":
    print("El numero de pulsaciones del señor" ,nombre ,"es de" ,numPulsacionesHombres ,"por cada 10 segundos")
elif genero == "femenino":
    print("El numero de pulsaciones de la señorita" ,nombre ,"es de" ,numPulsacionesMujeres ,"por cada 10 segundos")    
else:
    print("El genero no corresponde con la tabla")