class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        
        stones=[-stone for stone in stones]
        
        heapq.heapify(stones)
        
        while len(stones) >=2:
            y=heappop(stones)
            x=heappop(stones)
            if x !=y:
                heappush(stones, (y-x))
        
        return -1*stones[0] if stones else 0
    
                
        
        
        