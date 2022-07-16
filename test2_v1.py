# -*- coding: utf-8 -*-
from collections import Counter


def contar_letras_repetidas(texto):
    contador = Counter(texto)
    duplicados = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(duplicados)

texto = input('Escribe una palabra (V1): ')
print(contar_letras_repetidas(texto))

# Mi primer intento o versión fué contar las letras o la cadena
# para obtener el resultado deseado
