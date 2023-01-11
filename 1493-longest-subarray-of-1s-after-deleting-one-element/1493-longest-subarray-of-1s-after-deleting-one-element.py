class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best=left=right=current=0
        
        n=len(nums)
        
        while right < n:
            if nums[right]==0:
                current+=1
            while current > 1:
                if nums[left] ==0:
                    current-=1
                left+=1
            right+=1
            best=max(best, right-left-1)
           
        
        return best 
        
        
        
        