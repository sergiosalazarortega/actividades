def multiplicarString(cadena, n):
    if n <= 0:
        return ""
    else:
        return cadena * n

texto1 = "Hola"
repeticiones1 = 3
resultado1 = multiplicarString(texto1, repeticiones1)
print(resultado1)

texto2 = "Adios"
repeticiones2 = 5
resultado2 = multiplicarString(texto2, repeticiones2)
print(resultado2)
