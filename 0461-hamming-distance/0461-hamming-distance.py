class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        xor_res=x^y
        hamming=0
        
        while xor_res !=0:
            if (xor_res & 1)==1:
                hamming+=1
            xor_res>>=1
                
            
        
        
#         while x !=0 or y !=0:
            
#             if( (x>>1 | y >>1) == 1) and ((x>>1 & y >>1) !=1):
#                 hamming+=1
#             x>>=1
#             y>>=1
        
        return hamming
    
            
        
        