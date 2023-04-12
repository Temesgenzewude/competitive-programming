class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions=[(-1, 0), (1, 0), (0,-1), (0,1)]
        rows=len(image)
        cols=len(image[0])
        center=image[sr][sc]
        
        
        def dfs(row, col):
            image[row][col]=color
            
            def inboundAndValid(row,col):
                return 0 <= row < rows and 0 <= col < cols and image[row][col]==center
            
            
            for row_change, col_change in directions:
                new_row=row+row_change
                new_col=col+col_change
                
                if inboundAndValid(new_row, new_col):
                    dfs(new_row, new_col)
        if center == color:
            return image
        else:
            dfs(sr,sc)
        
        return image
        
        
                
            
            
            
        