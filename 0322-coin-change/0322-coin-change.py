class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        memo={}
        def dp(amount):
            if amount in memo:
                return memo[amount]
            
            if amount==0:
                return 0
            if amount < 0:
                return float("inf")
            ans=float("inf")
            for coin in coins:
                if amount-coin >= 0:
                    ans=min(ans, dp(amount-coin)+1)
                    
            memo[amount]=ans
            return memo[amount]
        
        
        result=dp(amount)
        
        return result if result !=float("inf") else -1
        
        
        
                    
            
            
            
            
        
        
        
        
        
            
                
        