# -*- coding: utf-8 -*-

### Using it like a Function ###
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
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        else:
            print(fizzbuzz)



if __name__ == "__main__" :
    fizzbuzz()