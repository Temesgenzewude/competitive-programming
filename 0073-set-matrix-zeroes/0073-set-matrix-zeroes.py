class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        zeros_pos=[]
        rows= len(matrix)
        cols=len(matrix[0])
        
        
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    zeros_pos.append((row, col))
       
        
        
        
        for zr, zc in zeros_pos:
            row=zr
            col=zc
            
            # go up
            while 0 <= row:
                matrix[row][col]=0
                row-=1
            row=zr
            # go down
            while row < len(matrix):
                matrix[row][col]=0
                row+=1
            # go right
            row=zr
            col=zc
            while col < len(matrix[0]):
                matrix[row][col]=0
                col+=1
            col=zc
            # go left
            while 0 <= col:
                matrix[row][col]=0
                col-=1
        
            
            
        
                    
                    
        