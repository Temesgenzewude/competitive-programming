class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dp(idx, currSum):
            if idx >= len(nums):
                if currSum==target:
                    return 1
                return 0
            if (idx, currSum) not in memo:
                memo[(idx, currSum)]=dp(idx+1, currSum+nums[idx])+ dp(idx+1, currSum- nums[idx])
            return memo[(idx, currSum)]
        
        return dp(0,0)
        
        
        
        
        
        
        