class Solution:
    def findComplement(self, num: int) -> int:
        
        mask=1
        
        new=num
        
        count=0
        
        
        
        while new !=0:
            count+=1
            new>>=1
       
            
    

        
        for i in range(count):
            num^=mask
            mask<<=1
        
        
#         while num!=0:
            
#             num ^= mask
#             print(num)
            
#             mask<<=1
            
        return num
        
        
        
        
        
        
        
        
        
        