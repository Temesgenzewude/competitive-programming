class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0:
            return False
        elif n== 1:
            return True
        else:
            
            while n % 3 == 0:
                if n /3 == 1:
                    return True
                else:
                    n= n/3
            return False
        
       
            
            
        