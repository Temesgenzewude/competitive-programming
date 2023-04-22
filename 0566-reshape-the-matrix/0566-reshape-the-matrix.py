class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n,m=len(mat), len(mat[0])
        
        result=[[0 for _ in range(c)] for _ in range(r)]
        
        if n*m != r*c:
            return mat
        
        row=col=0
        
        for i in range(n):
            for j in range(m):
                result[row][col]=mat[i][j]
                col+=1
                if col==c:
                    row+=1
                    col=0
        
        return result
                
                
                
        
        
        