import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1:
            return 1
        left=0
        right=x//2
        
        while right >=left:
            mid=left + (right-left)//2
            if mid**2==x:
                return mid
            elif mid**2 > x:
                right=mid-1
            else:
                left=mid+1
            
        return right
                
                
        
        
        
       
        