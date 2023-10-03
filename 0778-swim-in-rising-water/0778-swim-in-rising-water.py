class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        
        maxDepth=0
        
        
        queu=[(grid[0][0], 0, 0)]
        
        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        visited=set()
        
        visited.add((0,0))
        
        while queu:
            curH, row, col=heapq.heappop(queu)
            maxDepth=max(maxDepth, curH)
            
            if (row, col)== (n-1, n-1):
                break
                
            
            for r, c in directions:
                n_r= row+r
                n_c=col+c
                
                if 0<= n_r < n and 0<=n_c < n and (n_r, n_c) not in visited:
                    heapq.heappush(queu, (grid[n_r][n_c], n_r, n_c))
                    visited.add((n_r,n_c))
                    
        return maxDepth
                    
        