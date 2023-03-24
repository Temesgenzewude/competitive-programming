class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        def cyclicSort(nums):
            n=len(nums)
            result=[]

            for i in range(n):
                nums[abs(nums[i])-1]= -abs(nums[abs(nums[i])-1])
            
            
            for i in range(n):
                if nums[i]>0:
                    result.append(i+1)
                    
            return result
        
        return cyclicSort(nums)
        
                    

    

        
       
                
        