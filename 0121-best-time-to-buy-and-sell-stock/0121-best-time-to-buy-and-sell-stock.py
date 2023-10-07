class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit
        
        
        
#         buyAt=0
        
#         for i in range(len(prices)):
#             if prices[i] < prices[buyAt]:
#                 buyAt=i
        
#         if buyAt == len(prices)-1:
#             return 0
        
#         sellAt= buyAt
        
#         for i in range(buyAt+1, len(prices)):
#             if prices[i] > prices[sellAt]:
#                 sellAt= i
                
        
#         return prices[sellAt]-prices[buyAt]
    
            
        