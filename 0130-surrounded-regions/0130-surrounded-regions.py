class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        
        """
        
        n=len(board)
        m=len(board[0])
        directions=[(1,0), (-1,0), (0,1),(0,-1)]
        
        def dfs(row, col):
            if row <0 or col < 0 or row >=n or col >=m or board[row][col] != "O":
                return
            board[row][col]="T"
            for row_change, col_change in directions:
                dfs(row+row_change, col+col_change)
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i in [0,n-1] or j in [0,m-1]):
                    
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                    
        for i in range(n):
            for j in range(m):
                if board[i][j]=="T":
                    board[i][j]="O"
        
            
                    
        
        