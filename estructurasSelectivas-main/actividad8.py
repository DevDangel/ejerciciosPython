"""
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene 
anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que 
tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como 
negativo. La tabla en la que el médico se basa para obtener el resultado es la siguiente:
EDAD NIVEL HEMOGLOBINA
0-1 mes 13-26 g%
>1 y<= 6 meses 10-18 g%
> 6 y<= 12 meses 11-15 g%
>1 y<= 5 años  11.5-15 g%
>5 y<= 10 años 12.6-15.5 g%
> 10 y <= 15 años 13-15.5 g%
mujeres > 15 años 12-16 g%
hombres > 15 años 14-18 g%(octava)
"""
#Titulos
print("***RESULTADOS LABORATORIO MEDICO***")
paciente = input("Ingrese el nombre del paciente:\n")
################# PARA PODER INGRESAR DOS VALORES "NUMERO" Y "AÑO, AÑOS, MES O MESES"#####################
edad = input("Ingrese la edad el paciente(especifique en meses o años):\n")#Pedimos que ingrese el numero en enteros y seguido que ingrese, si es ("mes","meses","año","años") ej: ("2 meses") ("1 año") ("1 mes") ("5 años").
partes = edad.split()#Usamos el metodo .split() bajo la variable "partes" que contiene "edad" y divide o genera un espacio para que el usuario pueda ingresar dos valores.                                                                                   
edadNumero = int(partes[0])#La variable "edadNumero" almacena la primera parte [0] bajo el tipo de dato integer(int) osea almacena el numero que ingresa el usuario.
cadena = partes[1].lower()#La variable "cadena" almacena la segunda parte del metodo split [1] que contiene un tipo de dato cadena(String) es decir almacena la palabra que ingrese el usuario("mes","meses","año","años").
#con el metodo .lower() transformamos cualquier valor de tipo cadena que ingrese el usuario a minuscula.Para poder usarlo mas adelante en las condicionales (cadena == "mes") 
##########################################################################################################
#Variable que almacenan el sexo de la persona(masculino/femenino) con el metodo .lower()
genero = input("Ingrese el sexo del paciente(Masculino/Femenino):\n").lower()
#Variable que almacena el numero que ingrese el usuario cuando se le pida el numero de hemoglobina
hemoglobina = float(input("Ingrese el nivel de hemoglobina en porcentaje \"%\" de acuerdo a el ultimo examen medico realizado:\n"))

#Condicionales

#Primera condicional 0-1 mes 13-26 g%
################################ ↓↓↓ EJEMPLO PARA TODAS LAS CONDICIONALES ↓↓↓ ####################################################
#(> mayor) (< menor) (>= mayor e igual) (<= menor e igual) (== igual)                                                            #
if edadNumero >= 0 and edadNumero <= 1 and (cadena == "mes" or cadena == "meses") and hemoglobina >= 13 and hemoglobina <= 26:   #
    print("El paciente",paciente ,"no presenta anemia.")                                                                         #
     #si se encuentra en los valores entandares el paciente no tiene anemia                                                      #
elif edadNumero >= 0 and edadNumero <= 1 and (cadena == "mes" or cadena == "meses") and hemoglobina > 26:                        #
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")                     #
    #Si el paciente supera los 26 g% de hemoglobina puse que podria tener policitemia (Policitemia: Aumento excesivo de glóbulos #
    #rojos. Puede causar problemas circulatorios, trombosis y complicaciones)                                                    #
elif edadNumero > 1 and edadNumero <= 1 and  (cadena == "mes" or cadena == "meses")and hemoglobina < 13:                         #
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia")                                                         #
    #Si el paciente tiene por debajo de 13 g% de hemoglobina el resultado medico es positivo para anemia                         #
##################################################################################################################################
             
#Segunda Condicional >1 y<= 6 meses 10-18 g%
elif edadNumero > 1 and edadNumero <= 6 and (cadena == "mes" or cadena == "meses")and hemoglobina >= 10 and hemoglobina <= 18:    
    print("El paciente",paciente ,"no presenta anemia.")
elif edadNumero > 1 and edadNumero <= 6 and (cadena == "mes" or cadena == "meses")and hemoglobina > 18:
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")
elif edadNumero > 1 and edadNumero <= 6 and (cadena == "mes" or cadena == "meses") and hemoglobina < 10:
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia") 
#Tercera Condicional > 6 y<= 12 meses 11-15 g%
elif edadNumero > 6 and edadNumero <= 12 and (cadena == "mes" or cadena == "meses")and hemoglobina >= 11 and hemoglobina <=15:
    print("El paciente",paciente ,"no presenta anemia.")
elif edadNumero > 6 and edadNumero <= 12 and (cadena == "mes" or cadena == "meses")and hemoglobina > 15:
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")
elif edadNumero > 6 and edadNumero <= 12 and (cadena == "mes" or cadena == "meses")and hemoglobina < 11:
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia") 
#Cuarta Condicional >1 y<= 5 años 11.5-15 g%
elif edadNumero > 1  and edadNumero <= 5 and (cadena == "año" or cadena == "años") and hemoglobina >= 11.5 and hemoglobina <= 15:
    print("El paciente",paciente ,"no presenta anemia.")
elif edadNumero > 1  and edadNumero <= 5 and (cadena == "año" or cadena == "años") and hemoglobina > 15:
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")
elif edadNumero > 1  and edadNumero <= 5 and (cadena == "años" or cadena == "años") and hemoglobina < 11.5:
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia") 
#Quinta condicional >5 y<= 10 años 12.6-15.5 g%
elif edadNumero > 5  and edadNumero <= 10 and (cadena == "año" or cadena == "años") and hemoglobina >= 12.6 and hemoglobina <= 15.5:
    print("El paciente",paciente ,"no presenta anemia.")
elif edadNumero > 5  and edadNumero <= 10 and (cadena == "año" or cadena == "años") and hemoglobina > 15.5:
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")
elif edadNumero> 5  and edadNumero <= 10 and (cadena == "año" or cadena == "años") and hemoglobina < 12.6:
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia") 
#Sexta condicional > 10 y <= 15 años 13-15.5 g%
elif edadNumero > 10  and edadNumero <= 15 and (cadena == "año" or cadena == "años") and hemoglobina >= 13 and hemoglobina <= 15.5:
    print("El paciente",paciente ,"no presenta anemia.")    
elif edadNumero > 10  and edadNumero <= 15 and (cadena == "año" or cadena == "años") and hemoglobina > 15.5:
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")
elif edadNumero > 10  and edadNumero <= 15 and (cadena == "año" or cadena == "años") and hemoglobina < 13:
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia")
###################################/SI EL PACIENTE TIENE MAS DE 15 AÑOS ESPECIFICAR EL GENERO(MASCULINO/FEMENINO)/#########################    
#Septima condicional mujeres > 15 años 12-16 g%                                                                                           #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "femenino" and hemoglobina >= 12 and hemoglobina <= 16:      #
    print("El paciente",paciente ,"no presenta anemia.")                                                                                  #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "femenino" and hemoglobina > 16:                             #
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")                              #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "femenino" and hemoglobina < 12:                             #
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia")                                                                  #
#Octava y ultima condicional hombres > 15 años 14-18 g%                                                                                   #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "masculino" and hemoglobina >= 14 and hemoglobina <= 18:     #
    print("El paciente",paciente ,"no presenta anemia.")                                                                                  #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "masculino" and hemoglobina > 18:                            #
    print("El paciente",paciente,"tiene un nivel de hemoglobina alta posible cuadro clinico de Policitemia")                              #
elif edadNumero > 15 and (cadena == "año" or cadena == "años") and genero == "masculino" and hemoglobina < 14:                            #
    print("El paciente",paciente,"presenta un cuadro clinico de Anemia")                                                                  #
###########################################################################################################################################
#Finalizamos la condicional con un mensaje por si digitó algo mal en algun campo
else:
    print("Ocurrio un error inesperado. (Revise nuevamente los datos que ingreso)")        