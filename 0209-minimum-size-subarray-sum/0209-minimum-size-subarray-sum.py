class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        slow=0
        prefixSum=0
        min_len=float("inf")
        n=len(nums)
        
        for fast in range(n):
            prefixSum+=nums[fast]
            
            while prefixSum >= target:
                min_len=min(min_len, fast- slow +1)
                prefixSum-=nums[slow]
                slow+=1
        return 0 if min_len == float('inf') else min_len
        
        
                
        