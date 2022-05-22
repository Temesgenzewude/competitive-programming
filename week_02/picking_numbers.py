


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
class Solution(object):
    def pickingNumbers(self,a):
        # Write your code here
        count=0
        # for i in range(len(a)):
        #     for j in range(len(a)):
        #         if i==j:
        #             continue
        #         elif abs(a[i]-a[j]<=1):
        #             count+=1
        # return count
        result=0
        visited = set()
        for i in range(len(a)):
            if i not in visited:
                maxCount = max(a.count(a[i]) + a.count(a[i] + 1), a.count(a[i]) + a.count(a[i] - 1))
                if maxCount > result:
                    result = maxCount
                visited.add(i)
        return result


def main():
    sol = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    nums2 = [1, 1, 1, 1]
    num1 = [1]
    arr = [3, 2, 4, 1, 1, 4, 5]
    arr2 = [1, 2, 3, 3, 5, 6, 3, 2]
    print(sol.pickingNumbers(nums2))
    # print(sol.topKFrequent(arr, 3))


main()
