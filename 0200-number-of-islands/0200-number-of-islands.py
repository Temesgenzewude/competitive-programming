class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count=0
       
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isInboundAndValid(row, col):
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]=="1"
        
        def dfs(row, col):
            
            grid[row][col]="0"
           
            # if isInboundAndValid(row, col) and (row, col) not in visited:
            #     visited.add((row, col))
            
            for row_change, col_change in directions:
                new_row=row+row_change
                new_col=col + col_change

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col]=="1":
                    dfs(new_row, new_col)
                    
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    
                    dfs(i,j)
                    count += 1
        return count
                    
                    
                    
                    
                    
        