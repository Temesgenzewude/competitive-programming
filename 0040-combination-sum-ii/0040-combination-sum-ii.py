class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        n=len(candidates)
        
        
        result=[]
       
        
        def backtrack(candidate,comb_sum, combination):
            if comb_sum==target:
                result.append(combination.copy())
                return
            
            if candidate == n or comb_sum> target:
                return
         
            
           
            
            combination.append(candidates[candidate])
            backtrack(candidate+1,comb_sum+candidates[candidate], combination)
            combination.pop()
           
            k=1
            while k+candidate<n and candidates[k+candidate]==candidates[candidate]:
                k=k+1
            backtrack(candidate+k, comb_sum, combination)
            

        
        backtrack(0,0,[])
        
        return result
            
            
        
        
        