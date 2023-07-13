class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        memo={}
        
        result=0
        
        for num in arr:
            if num-difference not in memo:
                memo[num]=1
            else:
                memo[num]=1+memo[num-difference]
            
            result=max(result, memo[num])
            
        return result
        