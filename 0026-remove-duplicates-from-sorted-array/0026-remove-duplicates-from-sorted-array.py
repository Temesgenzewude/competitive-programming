class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end=1
        start=0
        while end < len(nums):
            if nums[start]==nums[end]:
                nums.pop(end)
            else:
                start=end
                end+=1
        return len(nums)
        