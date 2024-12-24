# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

# Complete the 'simpleArraySum' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart

def simpleArraySum(codeList, shoppingCart):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    codeList_count = int(input().strip())

    codeList = []

    for _ in range(codeList_count):
        codeList_item = input()
        codeList.append(codeList_item)

    shoppingCart_count = int(input().strip())

    shoppingCart = []

    for _ in range(shoppingCart_count):
        shoppingCart_item = input()
        shoppingCart.append(shoppingCart_item)

    result = simpleArraySum(codeList, shoppingCart)

    fptr.write(str(result) + '\n')

    fptr.close()
