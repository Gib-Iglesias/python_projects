# -*- coding: utf-8 -*-


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

# Mi segundo intento o versión fué contar las letras o la cadena que el usuario pasara como input
# y tener varios ciclos que revisaran cada caso para obtener el resultado deseado
