class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2= s[::-1]
        s1=s
        
        n,m=len(s1), len(s2)
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]= max(dp[i][j+1], dp[i+1][j])
                    
        return dp[n][m]
        
        
        
        
    