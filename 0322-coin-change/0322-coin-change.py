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
        
        
#         result=dp(amount)
        
#         return result if result !=float("inf") else -1
        
        arr=[float("inf") for _ in range(amount+1)]
        arr[0]=0
        
        
        for i in range(amount+1):
            ans=float("inf")
            # print(i)
            for coin in coins:
                if i-coin >= 0:

                    ans=min(ans, arr[i-coin]+1)
            arr[i]=min(ans, arr[i])
       
            
        return arr[-1] if arr[-1] !=float("inf") else -1
        
            
        
        
        
                    
            
            
            
            
        
        
        
        
        
            
                
        