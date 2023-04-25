class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions=[(-1,0), (1,0),(0,-1),(0,1)]
        
    
        
        
        
        def isInboundAndValid(row, col):
            return 0 <= row < len(grid2) and 0<=col < len(grid2[0]) and grid2[row][col]==1
        
        visited=set()
        
        
        
        def dfs(row, col):
            
            if row < 0 or col < 0 or row >= len(grid2) or col >= len(grid2[0]) or grid2[row][col]==0 or (row, col) in visited:
                return True
            visited.add((row, col))
            
            
            result=True
            if grid1[row][col]==0:
                result=False
           
            
            for row_change, col_change in directions:
                new_row=row+row_change
                new_col=col+ col_change
                
                result=dfs(new_row, new_col) and result
            
            return result
                
                
                    
        sub_islands=0
     
        
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if  grid2[row][col]==1 and (row, col) not in visited and dfs(row, col):
                    sub_islands += 1

        return sub_islands
        
        
        
        
#         directions=[(-1,0), (1,0),(0,-1),(0,1)]
        
#         self.isSubIland=True
        
        
        
#         def isInboundAndValid(row, col):
#             return 0 <= row < len(grid2) and 0<=col < len(grid2[0]) and grid2[row][col]==1
        
        
        
#         def dfs(row, col):
#             grid2[row][col]=0
#             grid1[row][col]=0
            
#             for row_change, col_change in directions:
#                 new_row=row+row_change
#                 new_col=col+ col_change
                
#                 if isInboundAndValid(new_row, new_col) and grid1[new_row][new_col]==1:
#                     dfs(new_row, new_col)
#                 elif isInboundAndValid(new_row, new_col) and grid1[new_row][new_col]==0:
#                     self.isSubIland=False
#                     return 
                    
#         sub_islands=0
     
        
#         for row in range(len(grid2)):
#             for col in range(len(grid2[0])):
#                 if grid2[row][col]==1 and grid1[row][col]==1:
                    
#                     dfs(row, col)
#                     if self.isSubIland:
#                         sub_islands += 1
#                 self.isSubIland=True
#         return sub_islands
                    
                
                
        