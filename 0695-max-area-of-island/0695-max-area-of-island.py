class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        self.max_area=0
        
        self.area=0
        
        directions=[(-1,0), (1, 0), (0,-1), (0,1)]
        
        def dfs(row, col):
            self.area+=1
            
            grid[row][col]=0
            
            for row_change, col_change in directions:
                new_row, new_col=row+row_change, col + col_change
                
                if 0 <= new_row < rows and 0<= new_col < cols and grid[new_row][new_col]==1:
                    dfs(new_row, new_col)
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    self.area=0
                    dfs(row, col)
                    self.max_area=max(self.max_area, self.area)
        return self.max_area
                    
                    
                    
            
                    
            
            
            
            
        