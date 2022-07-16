# -*- coding: utf-8 -*-
from collections import Counter


def contar_letras_repetidas(texto):
    contador = Counter(texto)
    duplicados = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(duplicados)

texto = input('Escribe una palabra (V1): ')
print(contar_letras_repetidas(texto))




def contador_letras():
    palabra = input('Escribe una palabra (V2): ')
    letras_dic = dict()
    contador = 0

    for letra in palabra:
        if letra in letras_dic:
            if letras_dic[letra] == 1:
                contador += 1
            letras_dic[letra] += 1
        else:
            letras_dic[letra] = 1

        if letras_dic[letra] > 1:
            print(letra)
        elif letras_dic[letra] == 0:
            contador = None
            print(contador)
    return contador

print('Letras Repetidas: ',contador_letras())

