# -*- coding: utf-8 -*-


def run():
    year = input('Ingresa el year: ') #año que queremos comprobar
    year = int(year)
    if year % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")
    return year


if __name__ == "__main__" :
    run()