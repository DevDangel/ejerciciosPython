"""
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad 
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo 
dígito de la placa de cada carro, se puede determinar el color de la calcomanía 
utilizando la siguiente relación: 
DIGITO                  CODIGO:
1 o 2                      amarilla 
3 o 4                      rosa
5 o 6                      roja
7 o 8                      verde
9 o 0                      azul
"""
# Inicializamos los contadores para cada color de calcomanía
amarilla = 0  # Contador para autos con calcomanía amarilla
rosa = 0      # Contador para autos con calcomanía rosa
roja = 0      # Contador para autos con calcomanía roja
verde = 0     # Contador para autos con calcomanía verde
azul = 0      # Contador para autos con calcomanía azul

# Pedimos al usuario el número total de autos
numero = int(input("¿Cuántos autos entran a la ciudad? "))

# Verificamos que el número total de autos sea mayor que cero
if numero <= 0:
    print("El número total de autos debe ser mayor que cero. Inténtalo de nuevo.")
else:
    # Usamos un bucle para procesar cada auto uno por uno
    for i in range(numero):
        # Pedimos el último dígito de la placa del auto al usuario
        digito = int(input(f"Ingrese el último dígito de la placa del auto {i + 1}: "))
        
        # Determinamos el color de la calcomanía basado en el último dígito
        if digito == 1 or digito == 2:
            amarilla += 1  # Si el dígito es 1 o 2, incrementamos el contador de calcomanías amarillas
        elif digito == 3 or digito == 4:
            rosa += 1      # Si el dígito es 3 o 4, incrementamos el contador de calcomanías rosas
        elif digito == 5 or digito == 6:
            roja += 1      # Si el dígito es 5 o 6, incrementamos el contador de calcomanías rojas
        elif digito == 7 or digito == 8:
            verde += 1     # Si el dígito es 7 u 8, incrementamos el contador de calcomanías verdes
        elif digito == 9 or digito == 0:
            azul += 1      # Si el dígito es 9 o 0, incrementamos el contador de calcomanías azules
        else:
            # Si el dígito ingresado no es válido, mostramos un mensaje de error
            print("Dígito no válido. Por favor, ingresa un dígito del 0 al 9.")
            # Decrementamos el índice del bucle para repetir la entrada actual
            i -= 1

    # Mostramos el total de autos para cada color de calcomanía
    print(f"Cantidad de autos con calcomanía amarilla: {amarilla}")
    print(f"Cantidad de autos con calcomanía rosa: {rosa}")
    print(f"Cantidad de autos con calcomanía roja: {roja}")
    print(f"Cantidad de autos con calcomanía verde: {verde}")
    print(f"Cantidad de autos con calcomanía azul: {azul}")
