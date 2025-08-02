# -*- coding: utf-8 -*-

"""
This script defines a function to extract even numbers from a list.
It iterates through the list, checks if each number is an integer or float, and if it is even, adds it to a new list.
The function returns this list of even numbers.
"""


def get_pairs(list):
    nums = []
    for num in list:
        if (isinstance(num, (int, float))) and (num % 2 == 0):
            nums.append(num)
    return nums

#Ejemplo1:
list1 = [1, 2, 3, 4, 5, 6, -2, -7, 0]
pair1 = get_pairs(list1)
print(f"Números pares en {list1}: {pair1}")

#Ejemplo2:
list1 = [1, 3, 5, 7, 9, 11, 13, 15]
pair1 = get_pairs(list1)
print(f"Números pares en {list1}: {pair1}")

#Ejemplo3:
list1 = [2, 4, 6, 8, 10, 12, 14, 16]
pair1 = get_pairs(list1)
print(f"Números pares en {list1}: {pair1}")
