# -*- coding: utf-8 -*-


def isValid(s: str) -> bool:
    close_map = {"(":")","{":"}","[":"]"}
    opens = []

    for symbol in s:
        if symbol in close_map.keys():
            opens.append(symbol)
        elif opens == [] or symbol != close_map[opens.pop()]:
            return False
    return opens == []


if __name__ == '__main__':
    # Exampple Array1: ([](){})
    # Exampple Array2: ([](){})]
    # Exampple Array3: ([{]([]){}})
    isValid = isValid(input('Escribe la cadena a revisar: '))
    print('Valid String? ',isValid)
