class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        result=[]
        
        for i in range(n):
            index=abs(nums[i])-1
            
            if nums[index] <0:
                result.append(index+1)
                
            
            
            nums[index]=-(nums[index])
            
            
            
        
        
        return result
        
        
    
        
        