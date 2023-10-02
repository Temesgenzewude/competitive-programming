class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        stoneSum= sum(stones)
        
        target=ceil(stoneSum/2)
        
        dp={}
        
        def dfs(idx, total):
            if total >=target or idx >= len(stones):
                return abs((2*total)-stoneSum)
            if (idx, total) in dp:
                return dp[(idx, total)]
            
            dp[(idx, total)]= min(dfs(idx+1, total), dfs(idx+1, total+stones[idx]))
            
            return dp[(idx, total)]
        
        
        return dfs(0,0)
    
        