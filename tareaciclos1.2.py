# Inicializar variables para almacenar la suma y la cantidad de números ingresados
suma = 0
cantidad_numeros = 0

# Leer números del teclado hasta que se ingrese 0
while True:
    numero = float(input("Ingrese un número (o 0 para salir): "))
    
    # Si se ingresa 0, salir del bucle
    if numero == 0:
        break
    
    # Sumar el número ingresado a la suma total
    suma += numero
    cantidad_numeros += 1

# Calcular el promedio
if cantidad_numeros > 0:
    promedio = suma / cantidad_numeros
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números para calcular el promedio.")
