class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        rows, cols=len(strs), len(strs[0])
        
        deletedCount=0
        
        for i in range(cols):
            for j in range(1, rows):
                if strs[j][i] < strs[j-1][i]:
                    deletedCount+=1
                    break
        return deletedCount
        