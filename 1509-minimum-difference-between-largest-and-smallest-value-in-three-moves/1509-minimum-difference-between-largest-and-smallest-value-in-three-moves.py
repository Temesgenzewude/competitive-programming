class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n <=4:
            return 0
        
        
        nums.sort()
        
        min_diff=float("inf")
        
        min_diff=min(min_diff, nums[n-1]-nums[3])
        min_diff=min(min_diff, nums[n-4]-nums[0])
        min_diff=min(min_diff, nums[n-2]-nums[2])
        min_diff=min(min_diff, nums[n-3]-nums[1])
        
        return min_diff
    
        
        
        
        
    
        
        
        
        
        