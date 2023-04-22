class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        n,m=len(matrix), len(matrix[0])
        
        def isScalar(row,col):
            first=matrix[row][col]
            
            while row < n and col < m:
                if matrix[row][col] != first:
                    return False
                row+=1
                col+=1
            return True
        
        
        for col in range(m):
            if not isScalar(0,col):
                return False
        for row in range(1, n):
            if not isScalar(row,0):
                return False
        
        return True
        
       
        