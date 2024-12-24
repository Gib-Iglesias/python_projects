# -*- coding: utf-8 -*-

def palindromo():
    text = input('Escribe una palabra: ')
    splited = list(text)
    #print('split: ',splited)
    inverted = splited[::-1]
    #print('reverse: ',inverted)
    str1 = ""
    joined = str1.join(inverted)
    #print('join: ',joined)
    return (joined == text)

print('Es un palíndromo?? ', palindromo())



def invertir_texto(texto):
    invertido = ''
    for letra in texto:
        invertido = letra + invertido
    print('texto_invertido: ',invertido)
    return invertido

invertir_texto('abcdefghij.klm')


# Palindromo en pagina de codigo (Hackerrank, Leetcode, etc)
def solution(inputString):
    splited = list(inputString)
    inverted = splited[::-1]
    str1 = ""
    joined = str1.join(inverted)
    return (joined == inputString)


# Dada una cadena de texto (str), invertirlo sin usar métodos propios del LP
def invertir_sm(texto):
    textoi = ''
    for letra in texto:
        textoi = letra + textoi
        print('Texto I: ', textoi)
    return textoi

invertir_sm('holaa')