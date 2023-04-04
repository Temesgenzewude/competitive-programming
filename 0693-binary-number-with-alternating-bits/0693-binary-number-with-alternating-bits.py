class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        rem=n %2
        q=n//2
        
        while q:
            if q%2 == rem:
                return False
            rem=q%2
            q=q//2
        return True
            
        
#         y= n  & 1
        
        
        
#         for i in range(n.bit_length()):
        
#             if y ==( n >> 1 & 1):
#                 return False
            
#             n >>=1
#             y= n & 1
        
#         return True
            
            
            
        