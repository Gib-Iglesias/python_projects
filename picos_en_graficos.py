def contar_picos(registros):
    """
    Cuenta la cantidad de picos superiores o inferiores en una lista de números.
    Un pico se define como un punto donde la diferencia absoluta
    entre el registro actual y el anterior es >= 5, Y la diferencia
    absoluta entre el registro actual y el siguiente es >= 5.
    """
    if len(registros) < 3:
    # Necesitamos al menos 3 puntos para tener un "anterior" y un "siguiente"
        return 0

    cantidad_picos = 0
    # Iteramos desde el segundo elemento hasta el penúltimo para poder comparar con el anterior y el siguiente.
    for i in range(1, len(registros) - 1):
        actual = registros[i]
        anterior = registros[i - 1]
        siguiente = registros[i + 1]

        # Calculamos las diferencias absolutas
        diff_anterior = abs(actual - anterior)
        diff_siguiente = abs(actual - siguiente)

        # Verificamos si cumple la condición de pico
        if diff_anterior >= 5 and diff_siguiente >= 5:
            cantidad_picos += 1

    return cantidad_picos

# Ejemplo1:
input_list = [8, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7]
picos_encontrados = contar_picos(input_list)
print(f"La lista: {input_list}")
print(f"Cantidad de picos: {picos_encontrados}") # Return 3
print("-" * 30)

# Ejemplo con menos picos
lista_ejemplo_2 = [1, 2, 3, 10, 5, 12, 1, 20, 10]
picos_encontrados_2 = contar_picos(lista_ejemplo_2)
print(f"La lista: {lista_ejemplo_2}")
print(f"Cantidad de picos: {picos_encontrados_2}") # Return 2
print("-" * 30)

# Ejemplo sin picos
lista_sin_picos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
picos_sin = contar_picos(lista_sin_picos)
print(f"La lista: {lista_sin_picos}")
print(f"Cantidad de picos: {picos_sin}") # Return 0
print("-" * 30)

# Ejemplo con pocos elementos
lista_corta = [10, 20]
picos_cortos = contar_picos(lista_corta)
print(f"La lista: {lista_corta}")
print(f"Cantidad de picos: {picos_cortos}") # Return 0
