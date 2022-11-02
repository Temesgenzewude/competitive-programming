class Solution:
    def longestOnes(self, nums, k):
        beg, end, zeroes, ans = 0, 0, 0, 0
        while end < len(nums):
            if zeroes + (nums[end] == 0) <= k:
                zeroes += nums[end] == 0
                end += 1
                ans = max(ans, end - beg)
            else:
                zeroes -= nums[beg] == 0
                beg += 1  
        return ans