# -*- coding: utf-8 -*-

# sqrt para calcular raices cuadradas
from math import sqrt


def fib():
    n = int(input("Ingresa el número de la serie buscado: "))
    if n < 2:
        return n
    else:
        u = ((1+sqrt(5))/2)
        j = ((u**n-(1-u)**n)/sqrt(5))
        # round nos permite redondear numeros flotantes
        print(round(j))
        return round(j)


if __name__ == "__main__" :
    fib()
