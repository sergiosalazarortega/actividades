# Solicitar al usuario los datos de la llanta pentagonal
lado_pentagono = float(input("Ingrese la longitud del lado de la llanta pentagonal: "))
apotema_pentagono = float(input("Ingrese la longitud del apotema de la llanta pentagonal: "))

# Solicitar al usuario los datos de la llanta hexagonal
lado_hexagono = float(input("Ingrese la longitud del lado de la llanta hexagonal: "))
apotema_hexagono = float(input("Ingrese la longitud del apotema de la llanta hexagonal: "))

# Calcular el área de las llantas
area_pentagono = 0.5 * (5 * lado_pentagono) * apotema_pentagono
area_hexagono = 0.5 * (6 * lado_hexagono) * apotema_hexagono

# Comparar y determinar la llanta con mayor área
if area_pentagono > area_hexagono:
    figura_mayor = "pentagonal"
    area_mayor = area_pentagono
elif area_hexagono > area_pentagono:
    figura_mayor = "hexagonal"
    area_mayor = area_hexagono
else:
    figura_mayor = "ambas"
    area_mayor = area_pentagono  # También podríamos usar area_hexagono, ya que son iguales en este caso

# Imprimir el resultado
print("El área de la llanta pentagonal es:", area_pentagono)
print("El área de la llanta hexagonal es:", area_hexagono)

if figura_mayor == "ambas":
    print("Ambas llantas tienen el mismo área.")
else:
    print("La llanta", figura_mayor, "tiene un área mayor de", area_mayor)