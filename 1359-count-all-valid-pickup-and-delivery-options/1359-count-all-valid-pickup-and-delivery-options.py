class Solution:
    def countOrders(self, n: int) -> int:
        
        dp=[0]*n
        
        dp[0]=1
        
        for i in range(1, n):
            j=2*(i+1)
            dp[i]=dp[i-1]*((j*(j-1))//2)
        
        return dp[n-1] % 1000000007
            
            
            
        