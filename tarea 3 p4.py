def main():
    user_input = int(input("Introduce un número entero: "))
    classification = []

    if user_input > 0:
        classification.append("positivo")
    else:
        classification.append("negativo")

    if user_input % 2 == 0:
        classification.append("par")
    else:
        classification.append("impar")

    if user_input < 100:
        classification.append("menor que 100")
    else:
        classification.append("mayor que 100")

    classification_str = ", ".join(classification)
    print(f"Es un número {classification_str}.")

if __name__ == "__main__":
    main()