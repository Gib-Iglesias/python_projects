# -*- coding: utf-8 -*-

def palindromo():
    text = input('Escribe una palabra: ')
    splited = list(text)
    inverted = splited[::-1]
    str1 = ""
    joined = str1.join(inverted)
    return (joined == text)

print('Es un palíndromo?? ', palindromo())

# Mi segundo intento o versión fué invertir las cadenas
# que el usuario pasara como input para obtener el resultado deseado
