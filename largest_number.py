# -*- coding: utf-8 -*-

# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Example
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# solution(inputArray) = 21.
# 7 and 3 produce the largest product.

def solution(inputArray):
    if len(inputArray) < 2:
        return None

    max_product = inputArray[0] * inputArray[1]

    for i in range(1, len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, product)

    return max_product

inputArray = [3, 6, -2, -5, 7, 3]
result = solution(inputArray)
print(result)
