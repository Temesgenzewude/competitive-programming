class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n=len(mat)
        m=len(mat[0])
        
        found=dict()
        
       
                    
                    
        
        
        
                          
                          
                          
                          
                          
                          
                    
        
        
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        
        
        
        
        result=[[0 for _ in range(m)] for _ in range(n)]
        
        def isInbound(row, col):
            
            return 0 <= row < n and 0 <= col < m
            
            
        
       
            
        visited=set()
            
        que=deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    que.append((i,j,0))


        while que:
            curr_len=len(que)
            
            for _ in range(curr_len):
                row, col,path=que.popleft()
                

                for row_change, col_change in directions:
                    new_row=row+row_change
                    new_col=col+col_change

                    if isInbound(new_row, new_col):
                        if mat[new_row][new_col]==1 and  (new_row, new_col) not in visited:
                            que.append((new_row, new_col, path+1))
                            result[new_row][new_col]= path+1
                            visited.add((new_row, new_col))
                            
        
        return result
                        
        
        
                        
                        
                    
                    
        