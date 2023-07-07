class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)
        m=len(matrix[0])
        
        memo={}
        
        
        def dfs(r, c, prevVal):
            if r < 0 or r==n or c<0 or c == m or matrix[r][c] <= prevVal:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            ans=1
            
            ans=max(ans, 1+dfs(r+1, c, matrix[r][c]))
            ans=max(ans, 1+dfs(r-1, c, matrix[r][c]))

            ans=max(ans, 1+dfs(r, c+1, matrix[r][c]))

            ans=max(ans, 1+dfs(r, c-1, matrix[r][c]))
            
            memo[(r,c)]=ans
            
            return ans
        
        result=float("-inf")
        for r in range(n):
            for c in range(m):
                result=max(result, dfs(r, c, -1))
                
        return result
                

            
        