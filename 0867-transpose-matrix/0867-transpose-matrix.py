class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        transpose=[[0 for i in range(rows)]  for j in range(cols)] 
        for i in range(rows):
            for j in range(cols):
                transpose[j][i]=matrix[i][j]
        
        return transpose

        