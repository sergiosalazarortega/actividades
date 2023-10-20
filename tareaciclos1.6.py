def es_divisible_por_243(numero):
    if numero % 243 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))
resultado = es_divisible_por_243(numero)
print(f"¿{numero} es divisible por 243? {resultado}")
