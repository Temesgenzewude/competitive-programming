class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        oneD=[]
        rows=len(matrix)
        cols=len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                oneD.append(matrix[i][j])
                
        def isGreater(mid):
            return oneD[mid] >target
        
        left=-1
        right=len(oneD)
        
        while right>left+1:
            mid=left + (right-left)//2
            mid_val=oneD[mid]
            
            if mid_val==target:
                return True
            elif isGreater(mid):
                right=mid
            else:
                left=mid
    
        
        return oneD[right]==target if right < len(oneD) else False
                
            
            
    
        