# -*- coding: utf-8 -*-


# Given a target number and a list of numbers, find two numbers in the list that sum to the target and return their indices

# # Sample Input
# list_of_nums = [0, 4, 2, 3, 5, 6]
# target = 5

# # Sample Output
# [(0, 4), (2,3)]


def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                print([i, j])


def twoSums(nums, target):
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            print([complementMap[num], i])
        else:
            complementMap[complement] = i


def twoSumHash(num_arr, pair_sum):
    hashTable = {}
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]


def rock(self):
    x = y = 'Python'
    x += 'rocks !!'
    print(x, y)



if __name__ == "__main__" :

    ### Function Type 1 ###
    nums = [1,2,3,4]
    target = 5
    two_sums(nums, target)

    ### Function Type 2 ###
    nums = [1,2,3,4]
    target = 5
    twoSums(nums, target)

    ### Function Type 3 ###
    num_arr = [1,2,3,4]
    pair_sum = 5
    twoSumHash(num_arr, pair_sum)

    ### Python Rocks ###
    rock(1)