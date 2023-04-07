class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        self.perimeter=0
        
        def inbound(row, col):
            
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid,row, col):
            
            visited[row][col] = True
            
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if not inbound(new_row,new_col)  or grid[new_row][new_col]==0:
                    self.perimeter+=1
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]==1:
                    dfs(grid, new_row, new_col)
            
        rw=cl=0   
        
        for i in range(len(grid)):
            found=False
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    found=True
                    rw=i
                    cl=j
                    break
            if found:
                break
        dfs(grid, rw,cl)
                    
        
        return self.perimeter
        
        
        