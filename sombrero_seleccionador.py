# -*- coding: utf-8 -*-
import csv
import random

class sombreroSeleccionador:

    def __init__(self):
        self.puntuaciones = [0,0,0,0]
        self.preguntas = []

    def cargar_preguntas(self, ruta):
        with open(ruta, newline='') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)
            for fila in lector_csv:
                self.preguntas.append(fila)

    def quiz(self):
        preguntas_aleatorias = random.sample(self.preguntas, 10)
        for pregunta in preguntas_aleatorias:
            opciones = [(pregunta[1], 0), (pregunta[2], 1), (pregunta[3], 2), (pregunta[4], 3)]
            random.shuffle(opciones)
            print(pregunta[0])
            for option in range(1,5):
                print(str(option) + '. ' + opciones[option-1][0])
            respuesta = int(input('Elige una opción del 1 al 4: '))
            self.puntuaciones[opciones[int(respuesta)-1][1]] += 1
        casas = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
        casa_asignada = casas[self.puntuaciones.index(max(self.puntuaciones))]
        casa_asignada = casa_asignada.upper()

        print('')
        print('###############################################################################')
        print('###############################################################################')
        print('')
        print('¡¡¡ Enhorabuena !!!   tu Casa en Hogwarts es:   ¡¡¡ '+casa_asignada,'!!!')
        print('')
        print('###############################################################################')
        print('###############################################################################')
        print('')

sombrero = sombreroSeleccionador()
sombrero.cargar_preguntas("preguntasV2.csv")
sombrero.quiz()
