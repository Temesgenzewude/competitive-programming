class Solution:
    def __init__(self):
        self.memo={0:0, 1:1,2:1}
    def tribonacci(self, n: int) -> int:
        
        return self.dp(n)
        
    def dp(self, n):
        if n not in self.memo:
            self.memo[n]=self.dp(n-1) + self.dp(n-2) + self.dp(n-3)
        return self.memo[n]
        
        
        