def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    user_input = int(input("Introduce un año: "))
    
    if es_bisiesto(user_input):
        print("Bisiesto")
    else:
        print("No bisiesto")

if __name__ == "__main__":
    main()