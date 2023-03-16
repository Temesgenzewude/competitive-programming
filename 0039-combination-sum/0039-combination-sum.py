class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        result=[]
        n=len(candidates)
        
        def backtrack(candidate, combination=[]):
            
            if sum(combination)==target:
                
                result.append(combination.copy())
                return 
            
            if candidate >=n or (target-sum(combination)) < candidates[candidate]: 
                return
            
            
            
                
            
            combination.append(candidates[candidate])
            backtrack(candidate, combination)
            combination.pop()
            backtrack(candidate+1, combination)
#             
            
#             if candidate >=n: 
#                 return
            
#             if sum(combination)==target:
#                 print(sum(combination))
#                 result.append(combination.copy())
#                 combination.pop()
#                 backtrack(candidate+1, combination)
#             elif sum(combination) > target:
#                 combination.pop()
#                 backtrack(candidate+1, combination)
#             elif sum(combination)< target:
#                 combination.append(candidates[candidate])
#                 backtrack(candidate, combination)
                
        
        backtrack(0)
        
        return result
            
            
            
                
                
        
        
        