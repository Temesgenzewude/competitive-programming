class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        
        self.reps=defaultdict(tuple)
        self.rank=[[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                self.reps[(i,j)]=(i,j)
        
        def isInbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def find(x):
            parent=self.reps[x]
            while parent != self.reps[parent]:
                parent=self.reps[parent]
            
            while x != self.reps[x]:
                self.reps[x]=parent
                x=self.reps[x]
            
            return parent
        
        def union(x,y):
            xRep=find(x)
            yRep=find(y)
            
            if xRep == yRep:
                return
            if self.rank[xRep[0]][xRep[1]]==self.rank[yRep[0]][yRep[1]]:
                self.rank[xRep[0]][xRep[1]]+=1
            if self.rank[xRep[0]][xRep[1]] > self.rank[yRep[0]][yRep[1]]:
                self.reps[yRep]=xRep
            else:
                self.reps[xRep]=yRep
                
                
        valid_right_path = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        valid_down_path = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}
        directions=[(1,0),(0,1)]
        
        for row in range(n):
            for col in range(m):
                for row_change, col_change in directions:
                    new_row=row+row_change
                    new_col=col+col_change
                    
                    if isInbound(new_row, new_col) and grid[new_row][new_col] in valid_right_path[grid[row][col]] and new_col-col==1:
                        union((row, col),(new_row, new_col))
                    if isInbound(new_row, new_col) and grid[new_row][new_col] in valid_down_path[grid[row][col]] and new_row-row==1:
                        union((row, col),(new_row, new_col))
                        
        
        return find((0,0))==find((n-1,m-1))
        
        
                
            
            
    
        
       
            
        