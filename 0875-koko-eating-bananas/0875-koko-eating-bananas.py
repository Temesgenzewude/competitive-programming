class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(pi, k, h):
            total_time=sum([math.ceil(pile/k) for pile in piles] )
            return total_time <=h
        
        low=0
        high=max(piles)+1
        
        while high > low+1:
            mid=low + (high-low)//2
            if canEat(piles, mid, h):
                high=mid
            else:
                low=mid
        
        return high
        