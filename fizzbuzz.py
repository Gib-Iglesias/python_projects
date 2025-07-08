# -*- coding: utf-8 -*-


### Using FizzBuzz like a Function ###
#def fizz_buzz(input):
#	if (input % 3 == 0) and (input % 5 == 0):
#		return "FizzBuzz"
#	if input % 3 == 0:
#		return "Fizz"
#	if input % 5 == 0:
#		return "Buzz"
#	return input
#
#print(fizz_buzz(input))


# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers that are multiples of both three and five output “FizzBuzz”.
def fizzbuzz():
    for fizzbuzz in range(101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        else:
            print(fizzbuzz)


if __name__ == "__main__" :
    fizzbuzz()




#!/bin/python3
import math
import os
import random
import re
import sys

#Python3
#FizzBuzz Problem
#HackerRank
# Complete the 'fizzBuzz' function below
# The function accepts INTEGER n as parameter

def fizzbuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzbuzz(n)





# Using NodeJS for create FizzBuzz function:
"""
    function fizzBuzz(n) {
        for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz");
        } else if (i % 3 === 0) {
            console.log("Fizz");
        } else if (i % 5 === 0) {
            console.log("Buzz");
        } else {
            console.log(i);
        }
        }
    }
"""
# Using node only need to change the way you send the parameter in the function
