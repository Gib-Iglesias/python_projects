# -*- coding: utf-8 -*-

def invertir_texto(texto):
    invertido = ''
    for letra in texto:
        invertido = letra + invertido
    print('texto_invertido: ',invertido)
    return invertido

invertir_texto('abcdefghij.klm')

# Mi primer intento o versión fué doblar o invertir
# el texto o cadena para obtener el resultado
