# -*- coding: utf-8 -*-

def simpleArraySum(ar):
    sums = 0
    for element in ar:
        sums += element
    return sums

list_a = [1,2,3,4,5,6,7,8,9,0]
print(simpleArraySum(list_a))

list_b = [5,4,3,2,1,0]
print(simpleArraySum(list_b))
