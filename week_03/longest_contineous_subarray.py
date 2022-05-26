
'''
Given an array of integers nums and an integer limit,
return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
'''

from collections import deque

class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        # max_len = 1
        # maxi = nums[0]
        # mini = nums[0]
        # temp = nums[0:1]
        # for i in range(1, len(nums)):
        #     temp.append(nums[i])
        #     if nums[i] > maxi:
        #         maxi = nums[i]
        #     if nums[i] < mini:
        #         mini = nums[i]
        #
        #     if maxi - mini <= limit:
        #         if len(temp) > max_len:
        #             max_len = len(temp)
        #     else:
        #         temp.pop(0)
        #         while max(temp) - min(temp) > limit:
        #             temp.pop(0)
        #         maxi = max(temp)
        #         mini = min(temp)
        #
        # return max_len
        result=0
        left=0
        right=0
        increasing_queue=deque()
        decreasing_queue=deque()
        while right<len(nums):
            while decreasing_queue and nums[decreasing_queue[-1]]<=nums[right]:
                decreasing_queue.pop()
            while increasing_queue and nums[increasing_queue[-1]]>=nums[right]:
                increasing_queue.pop()
            increasing_queue.append(right)
            decreasing_queue.append(right)

            while nums[decreasing_queue[0]]-nums[increasing_queue[0]]> limit:
                left+=1
                if left > increasing_queue[0]: increasing_queue.popleft()
                if left> decreasing_queue[0]: decreasing_queue.popleft()
            result=max(result, right-left+1)
            right+=1
        return result



if __name__ == '__main__':
    sol=Solution()
    nums=[1, 3, 4,2, 7, 6]
    result=sol.longestSubarray(nums, 5)
    print(result)

