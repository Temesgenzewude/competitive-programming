class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo={}
        def dp(i, start):
            
            
            if i < start:
                return 0
            if i==start:
                return nums[start]
            if i==start+1:
                return max(nums[start], nums[start+1])
            
            if (i, start) not in memo:
                memo[(i, start)]=max((nums[i]+max(dp(i-2, start), dp(i-3, start)), dp(i-1, start)))
            return memo[(i, start)]
        
        if len(nums) < 4:
            return max(nums)
        
        return max(dp(len(nums)-1,1), dp(len(nums)-2,0))
        
        
        
        