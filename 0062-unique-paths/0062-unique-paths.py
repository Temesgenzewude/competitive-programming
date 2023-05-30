class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo={}
        
        def inbound(row, col):
            return 0<= row < m and 0 <= col < n
        
        def dp(row, col):
            if row == m or col == n:
                return 1
            if inbound(row, col) and (row, col) not in memo:
                memo[(row, col)]= dp(row, col+1)+ dp(row+1, col)
            if inbound(row, col):
                return memo[(row, col)]
        
        return dp(1,1)
        
            
        
        