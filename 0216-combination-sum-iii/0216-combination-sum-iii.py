class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result=[]
        
        def backtrack(candidate, combination=[]):
            
            if len(combination)==k and sum(combination)==n:
                result.append(combination.copy())
                return
            
            if len(combination) > k or sum(combination) > n or candidate==10:
                return 
            
            
            
            
            
            combination.append(candidate)
            backtrack(candidate+1, combination)
            combination.pop()
            backtrack(candidate+1, combination)
            
            
        backtrack(1)
        
        
        return result
            
        
        