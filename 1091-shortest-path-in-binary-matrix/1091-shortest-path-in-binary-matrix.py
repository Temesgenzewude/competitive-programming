class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        
        directions=[(-1,-1),(-1,0),(0,-1),(1,-1), (-1, 1),(1,1), (1, 0), (0,1)]
        
        def isInboundAndValid(row, col):
            return 0 <= row < n and 0 <=col < n and grid[row][col]==0
        
        
        
        def bfs(grid):
      
            que=deque()
            que.append((0,0,1))

            while que:
                
                
                row, col, path=que.popleft()
                if (row, col)==(n-1, n-1):
                    return path
                
                for row_change, col_change in directions:
                    new_row=row+row_change
                    new_col=col+ col_change
                    
                    if isInboundAndValid(new_row, new_col):
                        grid[new_row][new_col]=1
                        
                        que.append((new_row, new_col, path+1))
                      
                
           
            
                
            return -1
        
        return bfs(grid)
        
        
                
                
                    
                    
            
            
           
        