class Solution:
    

        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        self.memo={n:0, n+1:0}

        
        def dp(n):
   
            if n not in self.memo:
                self.memo[n]=cost[n] +min(dp(n+1),dp(n+2))
            return self.memo[n]
        dp(0)
        return min(self.memo[0],self.memo[1])
        