# -*- coding: utf-8 -*-
import os
import random

def run():

    DB = [
        'CERDO',
        'PERICO',
        'LEOPARDO',
        'PERRO',
        'GATO',
        'ZORRO',
        'IGUANA',
        'PESCADO',
        'PULPO',
        'CAMALEON',
        'ELEFANTE',
        'HIPOPOTAMO',
        'ZEBRA',
        'FLAMINGO',
        'CANGURO',
        'ORNITORRINCO',
        'BALLENA',
        'CACHALOTE',
        'OSO',
        'ABEJA',
        'MOSQUITO',
        'MOSCA',
        'MORSA',
        'CALAMAR',
        'CANGREJO',
        'CABALLO',
        'CABRA',
        'VACA',
        'CORDERO',
        'OVEJA',
        'GALLO',
        'AGUILA',
        'ANGUILA',
        'HALCON',
        'GAVIOTA'
    ]

    IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra:  ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("clear")
            print("Palabra Oculta: ",word)
            print("¡¡¡¡¡ Felicidades !!!!!")
            print("¡¡¡ Encontraste la palabra oculta y salvaste a tu personita !!!")
            print("¡¡¡¡¡ Ganaste !!!!!")
            break
            input()

        if attemps == 0:
            os.system("clear")
            print("Palabra Oculta: ",word)
            print("¡ Lo siento Perdiste :( !")
            print("¡¡¡ No Encontraste la palabra oculta y tu personita fué ahorcada")
            break
            input()


if __name__ == "__main__" :
    run()
