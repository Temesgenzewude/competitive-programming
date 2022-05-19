'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose
sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count=0
        # visited=[]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         elif nums[i] + nums[j]==k and (i, j) not in visited and (j, i) not in visited:

        #             visited.append((i, j))
        #             count+=1
        # return count
        count = 0
        dic = {}
        for num in nums:
            dif = k - num
            if dif in dic and dic[dif] > 0:
                count += 1
                dic[dif] -= 1
            else:
                if num not in dic:
                    dic[num] = 0
                dic[num] += 1
        return count


def main():
    sol = Solution()
    nums = [3, 1, 3, 4, 2, 3, 3]
    k = 6
    print(sol.maxOperations(nums, k))


main()
