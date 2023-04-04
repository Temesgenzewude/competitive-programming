class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        y= n  & 1
        
        
        
        for i in range(n.bit_length()):
        
            if y ==( n >> 1 & 1):
                return False
            
            n >>=1
            y= n & 1
        
        return True
            
            
            
        