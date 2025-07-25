# -*- coding: utf-8 -*-

def largest_four(arr):
    if len(arr) < 4:
        return sum(arr)
    else:
        arr.sort(reverse=True)
        return sum(arr[:4])

print('Largest1: ', largest_four([1,1,1,-5]))
print('Largest2: ', largest_four([0,0,2,3,7,1]))
