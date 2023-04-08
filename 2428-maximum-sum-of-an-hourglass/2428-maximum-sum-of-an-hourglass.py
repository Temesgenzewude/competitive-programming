class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        max_sum=0
        
        def hourglassSum(i,j):
            return sum(grid[i-1][j-1: j+2]) + grid[i][j] + sum(grid[i+1][j-1: j+2])
        
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                max_sum=max(max_sum, hourglassSum(i,j))
        return max_sum
                
                
        