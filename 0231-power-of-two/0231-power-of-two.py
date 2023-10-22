class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n==1:
            return True
        x=2
        
        while x <=n:
            if x==n: return True
            
            x*=2
        return False
        