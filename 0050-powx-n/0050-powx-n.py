class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(base, exp):
            if base ==0: return 0
            
            exp=abs(exp)
            
            
            if exp==1:
                return x
            if exp==0:
                return 1
            
            half=helper(base, exp//2)
            
            return half*half* helper(base, exp%2)
        
        
        result=helper(x,n)
        
        if n <0:
            return 1/result
        
        return result
            
            
            
            
            
            
        
        
        
        