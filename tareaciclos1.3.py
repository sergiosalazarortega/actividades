# Solicitar al usuario la cantidad de artículos
n = int(input("Ingrese la cantidad de artículos: "))

# Inicializar una lista para almacenar los artículos
lista_compras = []

# Leer n artículos desde la terminal
for i in range(n):
    articulo = input(f"Ingrese el artículo {i + 1}: ")
    lista_compras.append(articulo)

# Ordenar la lista alfabéticamente
lista_compras.sort()

# Imprimir la lista en orden alfabético
print("\nLista de compras en orden alfabético:")
for articulo in lista_compras:
    print(articulo)
