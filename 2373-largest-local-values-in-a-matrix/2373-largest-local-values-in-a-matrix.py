class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        maxLocal=[[0 for _ in range(n-2)] for _ in range(n-2)]
        
        
        for i in range(n-2):
            for j in range(n-2):
                _max=grid[i+1][j+1]
                
                for ii in range(i,i+3):
                    for jj in range(j, j+3):
                        _max= max(_max, grid[ii][jj])
                maxLocal[i][j]=_max
        return maxLocal
        