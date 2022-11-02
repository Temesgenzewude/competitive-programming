class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]*len(nums)
        
        prefix = 1
        
        postfix = 1
        
        
        for i in range(0,len(nums)):
            
            ans[i] = prefix
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            
            ans[i] = ans[i]*postfix
            postfix*=nums[i]
           
        return ans