class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[1]
        
        for x, y in zip(prices, prices[1:]):
            if x == y+1:
                dp.append(dp[-1] +1)
            else:
                dp.append(1)
      
        return sum(dp)
            
        
        
        
        