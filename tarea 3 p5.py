arreglo = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']

# Accediendo a elementos por índice
primer_elemento = arreglo[0]  # 'Do'
segundo_elemento = arreglo[1]  # 'Re'
tercer_elemento = arreglo[2]   # 'Mi'

# Accediendo a elementos usando índices negativos (comenzando desde el final)
ultimo_elemento = arreglo[-1]  # 'Si'
penultimo_elemento = arreglo[-2]  # 'La'
antepenultimo_elemento = arreglo[-3]  # 'Sol'

# Accediendo a un rango de elementos
primeros_tres_elementos = arreglo[0:3]  # ['Do', 'Re', 'Mi']
elementos_desde_el_cuarto = arreglo[3:]  # ['Fa', 'Sol', 'La', 'Si']
elementos_hasta_el_quinto = arreglo[:5]  # ['Do', 'Re', 'Mi', 'Fa', 'Sol']