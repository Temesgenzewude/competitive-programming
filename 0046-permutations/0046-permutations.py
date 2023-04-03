class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        
        
        def helper(arr, perm):
            if not arr:
                
                result.append(perm)
            for i in range(len(arr)):
                helper(arr[:i] + arr[i+1:], perm+ [arr[i]])
               
            
            
           
            # else:
            #     for i in range(start, end):
            #         nums[start], nums[i]=nums[i], nums[start]
            #         helper(nums,start+1, end)
            #         nums[start], nums[i]= nums[i], nums[start]
            
        helper(nums, [])
        
        return result
    
            
                           
            
            
            
            
            
            
            
        
        
        