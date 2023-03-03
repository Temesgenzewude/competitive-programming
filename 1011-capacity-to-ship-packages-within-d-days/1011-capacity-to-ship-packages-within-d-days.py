class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def canShip(capacity):
            needed_days, currCap=1, capacity
            
            for weight in weights:
                if currCap - weight <0:
                    currCap=capacity
                    needed_days+=1
                currCap-=weight
            
            return needed_days <=days
            
        
        low=max(weights)-1
        high=sum(weights)+1
        
        while high > low +1:
            mid=low + (high-low)//2
            if canShip(mid):
                high=mid  
            else:
                low=mid
               
        return high
    
    
        
        
      
                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        