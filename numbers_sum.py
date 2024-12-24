# -*- coding: utf-8 -*-

# En la variable numbers tienes una lista de números.
# Implementa una función que devuelva un diccionario con la suma de los dígitos de cada número.
# Ejemplo {123: 6}

def sum_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def calculate_digit_sums(numbers):
    sum_digits_dict = {}
    for number in numbers:
        sum_digits_dict[number] = sum_digits(number)
    return sum_digits_dict

numbers = [123, 456, 789, 101, 202, 303]

result = calculate_digit_sums(numbers)
print(result)
