class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        n, m = len(grid), len(grid[0])
        ans = 0
        
        def magic(a,b,c,
                  d,e,f,
                  g,h,i):
            
            return (reduce(lambda d, c: d + 1 if 1<=c<=9 else 0, set([a,b,c,d,e,f,g,h,i]), 0) == 9 and
                (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))
        
        for i in range(n-2):
            for j in range(m-2):
                if magic(grid[i][j], grid[i][j+1], grid[i][j+2], 
                      grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], 
                      grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]) :
                    ans += 1
                       
        return ans
        