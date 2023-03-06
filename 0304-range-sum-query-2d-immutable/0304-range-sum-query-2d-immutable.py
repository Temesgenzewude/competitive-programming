class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.calculatePrefixSum()
    def calculatePrefixSum(self):
        rows= len(self.matrix)
        cols=len(self.matrix[0])
        
        #calculate colum sum
        for row in range(rows):
            for col in range(1,cols):
                self.matrix[row][col]= self.matrix[row][col]+self.matrix[row][col-1]
        
        for col in range(cols):
            for row in range(1, rows):
                self.matrix[row][col]=self.matrix[row][col]+self.matrix[row-1][col]
        print(self.matrix)
        
                
        
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.matrix[row2][col2]
        elif row1==0:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]
        elif col1==0:
            return self.matrix[row2][col2]-self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]-self.matrix[row1-1][col2]+self.matrix[row1-1][col1-1]
        
        
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)