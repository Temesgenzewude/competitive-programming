class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: 
                          int) -> int:
        
        return self.bellmanFord(n, flights, src, dst, k)
        
    def bellmanFord(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dists= [float('inf')] * n
        dists[src]=0
        
        for _ in range(k+1):
            
            tmpDists= dists.copy()
            
            for s, d, c in flights:
                if dists[s]== float('inf'):
                    continue
                if dists[s]+c < tmpDists[d]:
                    tmpDists[d]=dists[s]+c
            dists=tmpDists
            
        
        return -1 if dists[dst]== float('inf') else dists[dst]
                    