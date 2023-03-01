class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right=0, k-1
        min_diff=float("inf")
        
        while right < len(nums):
            min_diff=min(min_diff, nums[right]-nums[left])
            left, right= left+1, right+1
        return min_diff
        
    
        