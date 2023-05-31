class Solution:
    def __init__(self):
        self.memo={0:0, 1:1,2:1}
    def tribonacci(self, n: int) -> int:
        return self.bottomUp(n)
        
    def dp(self, n):
        if n not in self.memo:
            self.memo[n]=self.dp(n-1) + self.dp(n-2) + self.dp(n-3)
        return self.memo[n]
    
    
    
    
    
   
    def bottomUp(self, n):
        
        memo=[0 for i in range(n+1)]
        if n <= 1:
            return n
    
        memo[1], memo[2]=1,1
        for i in range(3,n+1):
            memo[i]=memo[i-1] + memo[i-2] + memo[i-3]
        return memo[-1]
    
        
        
        
        
        