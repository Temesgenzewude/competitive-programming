class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for idx, num in enumerate(nums):
            if num%2==0:
                nums[idx]=0
            else:
                nums[idx]=1
        
        
        odd_count={0:1}
        currSum=0
        count=0
    
        
        for num in nums:
            currSum+=num
            count+=odd_count.get(currSum-k,0)
            odd_count[currSum]=1+odd_count.get(currSum,0)
        
        return count
            
            
        