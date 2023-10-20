def main():
    # Crear un diccionario con los días en cada mes (año no bisiesto)
    days_in_month = {
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31
    }
    
    # Solicitar al usuario que ingrese un mes
    user_input = input("Introduce un mes: ").lower()
    
    # Obtener el número de días del mes ingresado
    if user_input in days_in_month:
        days = days_in_month[user_input]
        print(f"El mes de {user_input} tiene {days} días.")
    else:
        print("Mes no válido. Asegúrate de escribir el nombre completo del mes en minúsculas.")

if __name__ == "__main__":
    main()