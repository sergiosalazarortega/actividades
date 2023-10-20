def operacion_condicional(num1, num2, num3):
    if num1 > 100 or num2 > 100 or num3 > 100:
        return num1 + num2 + num3
    else:
        return num1 * num2 * num3

numero1 = 50
numero2 = 75
numero3 = 120
resultado1 = operacion_condicional(numero1, numero2, numero3)
print(f"Resultado 1: {resultado1}")

numero4 = 10
numero5 = 20
numero6 = 30
resultado2 = operacion_condicional(numero4, numero5, numero6)
print(f"Resultado 2: {resultado2}")
