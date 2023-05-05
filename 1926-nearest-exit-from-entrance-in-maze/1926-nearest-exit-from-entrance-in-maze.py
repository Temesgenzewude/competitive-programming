class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        def isInboundAndValid(row, col):
            return 0 <= row < N and 0 <= col < M and maze[row][col] == "."
        
        N, M = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
      
        queue = deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            row, col, distance = queue.popleft()
            
       
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                
               
                if isInboundAndValid(new_row, new_col):
                    
                    if 0 == new_row or new_row == N - 1 or 0 == new_col or new_col == M - 1:
                        return distance + 1
                    
                    maze[new_row][new_col] = "+"
                    queue.append([new_row, new_col, distance + 1])
       
        return -1
        