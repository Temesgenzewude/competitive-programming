class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets=[]
        
        
        def backtrack(idx, subset=[]):
            if idx >=len(nums):
                subsets.append(subset.copy())
                return
            subset.append(nums[idx])
            
            backtrack(idx+1,subset)
            subset.pop()
            backtrack(idx+1,subset)
        
        backtrack(0)
        
        return subsets
            
            
            
            
        