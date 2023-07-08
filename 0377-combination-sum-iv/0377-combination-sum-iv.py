class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        memo={0:1}
        
        for total in range(1, target+1):
            
            memo[total]=0
            for n in nums:
                memo[total]+=memo.get(total-n, 0)
                
        return memo[target]
        