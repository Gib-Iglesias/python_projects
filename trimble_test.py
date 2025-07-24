# -*- coding: utf-8 -*-


# *** CODE CHALLENGE 1 ****
# Write a Function that returns TRUE if a string begins with the Letter A, anything else should return a FALSE.

def starts_with_a(string):
	if string[0] == 'A' or string[0] == 'a':
		return True
	return False

print("Check1: ", starts_with_a("Alice"))
print("Check2: ", starts_with_a("Bob"))
print("Check3: ", starts_with_a("abracadabra"))


# *** CODING CHALLENGE 2 ****
# Write a function that returns the longest sequence of 1’s in an array
# containing 1’s and 0’s; array example a = [0,1,0,1,1,0,1,1,1,0,1]
# [0,1,0,1,1,0,1,0,1,1,1]

# Version1
def longest_ones(arr):
    long_chain = 0
    for i in range(len(arr)):
        if i == 1:
            long_chain += 1
        return long_chain

print("Longest Sequence1: ", longest_ones([0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]))
print("Longest Sequence2: ", longest_ones([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]))


#Version2
def longest_ones_new(arr):
    max_length = 0  # To store the maximum length found
    current_length = 0  # To store the current length of 1's sequence
    for num in arr:
        if num == 1:
            current_length += 1
        else:
            # If a 0 is encountered, reset current_length
            # but first update max_length if current_length is greater
            max_length = max(max_length, current_length)
            current_length = 0
    # After the loop, check one last time in case the array ends with 1s
    max_length = max(max_length, current_length)
    return max_length

# Ejemplos de uso:
a = [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
b = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
c = [1, 1, 1, 1, 0, 0, 1, 1]
d = [0, 0, 0, 0]
e = [1, 1, 1, 1]

print(f"Array a: {a} -> Longest sequence of 1's: {longest_ones_new(a)}")
print(f"Array b: {b} -> Longest sequence of 1's: {longest_ones_new(b)}")
print(f"Array c: {c} -> Longest sequence of 1's: {longest_ones_new(c)}")
print(f"Array d: {d} -> Longest sequence of 1's: {longest_ones_new(d)}")
print(f"Array e: {e} -> Longest sequence of 1's: {longest_ones_new(e)}")
