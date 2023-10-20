def main():
    # Crear una lista con los días de la semana en orden
    days_of_week = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    # Solicitar al usuario que ingrese un día de la semana
    user_input = input("Introduce un día de la semana: ").lower()
    
    # Obtener la posición del día en la semana
    if user_input in days_of_week:
        position = days_of_week.index(user_input) + 1
        print(f"El día {user_input} está en la posición {position} de la semana.")
    else:
        print("Día no válido. Asegúrate de escribir el nombre completo del día en minúsculas.")

if __name__ == "__main__":
    main()