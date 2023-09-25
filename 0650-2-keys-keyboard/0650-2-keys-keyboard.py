class Solution:
    def minSteps(self, n: int) -> int:
        
        dp = defaultdict(int)
        
        dp[0]=0
        dp[1]=0
        dp[2]=2
        dp[3]=3
        
        for i in range(4,n+1):
            dp[i]=i
            
            for j in range(2, i):
                if i%j==0:
                    dp[i]=min(dp[i], dp[i//j]+j)
                    
        return dp[n]
        