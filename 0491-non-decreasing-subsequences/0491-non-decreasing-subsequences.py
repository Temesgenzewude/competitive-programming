class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        result=set()
        
        def helper(idx, seq):
            if len(seq)>=2:
                result.add(tuple(seq))
        
            if idx >=len(nums):
                return
            
           
                
                
            if (seq and nums[idx] >=seq[-1]) or (not seq):
                seq.append(nums[idx])
                helper(idx+1, seq)
                seq.pop()
                
        
            helper(idx+1,seq)
                
           
            
            
        
        helper(0,[])
        solution=[]
        
        
        for res in result:
            solution.append(list(res))
        return solution
                
                
            
            
                
            
            
            
                
        