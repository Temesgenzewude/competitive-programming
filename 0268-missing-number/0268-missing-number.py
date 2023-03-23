class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(n):
            while nums[i]!=n and nums[i] !=i:
                nums[nums[i]], nums[i]=nums[i], nums[nums[i]]
                
        
        for i in range(n):
            if nums[i] !=i:
                return i
        
        return n
        
        
        
        
        
        
        