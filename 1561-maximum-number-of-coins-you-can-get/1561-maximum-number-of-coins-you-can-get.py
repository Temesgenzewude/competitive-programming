class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n=len(piles)
        left, right=0,n-1
        
        myCoins=0
        while left < right:
            myCoins+=piles[right-1]
            left+=1
            right-=2
        return myCoins
        
        
        