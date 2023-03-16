class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        n=len(candidates)
        
        
        result=[]
        visited=set()
        
        def backtrack(candidate, combination=[]):
            if sum(combination)==target:
                result.append(combination.copy())
                return
            
            if candidate == n or sum(combination)> target:
                return
            
            if candidates[candidate] in visited:
                backtrack(candidate+1, combination)
            
           
            
            combination.append(candidates[candidate])
            backtrack(candidate+1, combination)
            combination.pop()
            # visited.add(candidates[candidate])
            k=1
            while k+candidate<n and candidates[k+candidate]==candidates[candidate]:
                k=k+1
            backtrack(candidate+k, combination)
            
#             if candidates[candidate] in visited:
            
#                 visited.remove(candidates[candidate])
        
        backtrack(0)
        
        return result
            
            
        
        
        