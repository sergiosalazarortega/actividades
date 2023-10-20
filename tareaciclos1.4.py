# Solicitar al usuario la cantidad de números en la lista
n = int(input("Ingrese la cantidad de números en la lista: "))

# Inicializar una lista para almacenar los números
numeros = []

# Leer n números desde la terminal
for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Filtrar la lista para obtener solo los números pares
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

# Imprimir la lista de números pares
print("\nLista de números pares:")
for numero in numeros_pares:
    print(numero)
