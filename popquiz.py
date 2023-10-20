file_path = "output.txt"

with open(file_path, 'a') as file:
    file.write("Hola")
    file.write("\n")

print(f"Se escribió en '{file_path}' satisfactoriamente.")
