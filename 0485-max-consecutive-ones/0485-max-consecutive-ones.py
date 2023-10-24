class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] = nums[i] + nums[i - 1]
        
        return max(nums)