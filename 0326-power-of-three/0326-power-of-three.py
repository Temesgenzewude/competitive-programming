class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==1:
            return True
        elif n%3 !=0 or n <=0:
            return False
        return self.isPowerOfThree(n//3)
    
            
        
#         if n <= 0:
#             return False
#         elif n== 1:
#             return True
#         else:
            
#             while n % 3 == 0:
#                 if n /3 == 1:
#                     return True
#                 else:
#                     n= n/3
#             return False
        
#         mx= 3 **19
        
#         return n > 0 and mx % n ==0
        
       
            
            
        