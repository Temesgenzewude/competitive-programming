class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         count= {}
#         res, maxCount=0,0
        
#         for num in nums:
#             count[num]= 1 + count.get(num, 0)
            
#             if count[num] > maxCount:
#                 res= num
                
#             maxCount= max(count[num], maxCount)
            
#         return res 
    
        res, count=0, 0

        for num in nums:
            if count == 0:
                res= num
            if num== res:
                count+=1
            else:
                count-=1
        return res
    
    
        
        
                
                
           
        