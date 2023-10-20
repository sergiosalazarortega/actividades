
cadena = input("Ingrese una cadena de texto: ")


vocales = ""


vocales = "aeiouAEIOU"


for letra in cadena:
    if letra in vocales:
        vocales += letra


print("Vocales encontradas en la cadena:")
print(vocales)
