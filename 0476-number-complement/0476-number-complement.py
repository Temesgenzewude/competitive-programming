class Solution:
    def findComplement(self, num: int) -> int:
        
        mask=1
        m_sign=0
        
        
        for i in range(num.bit_length()):
            num^=mask
            mask<<=1
        
        
#         while num!=0:
            
#             num ^= mask
#             print(num)
            
#             mask<<=1
            
        return num
        
        
        
        
        
        
        
        
        
        