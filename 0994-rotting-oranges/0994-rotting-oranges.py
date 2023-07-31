class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshCount=0
        fresh=[]
        rotten=[]
        visited=set()
        rows, cols=len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    rotten.append((row, col))
                    visited.add((row, col))
                if grid[row][col]==1:
                    fresh.append((row, col))
        def isValid(row, col):
            return 0<=row<rows and 0<=col<cols and (row, col) not in visited and grid[row][col]==1
        
        def bfs():
            
            que=deque(rotten)
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            time=0
            freshCount=len(fresh)

            while que and freshCount>0:
                for _ in range(len(que)):

                    row, col=que.popleft()

                    for row_change, col_change in directions:
                        new_row=row+row_change
                        new_col=col+col_change

                        if isValid(new_row,new_col):
                            freshCount-=1
                            grid[new_row][new_col]=2
                            que.append((new_row, new_col))
                            visited.add((new_row, new_col))
                time+=1


            return time if freshCount==0 else -1
        
        return bfs()
                    
                    
        