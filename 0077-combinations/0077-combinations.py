class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result=[]
       
        
        def helper(candidate, combination_i=[]):
            
            
            
            if len(combination_i)==k:
                result.append(combination_i.copy())
                return
            if candidate>n:
                return
                
            # for i in range(candidate, n):
            combination_i.append(candidate)
            helper(candidate+1, combination_i)
            combination_i.pop()
            helper(candidate+1, combination_i)
            
            
        helper(1,[])
            
        return result
                
                
               
            
        
            
            
            
                
            
            
            
            
            
            
           
                
                
            
            
        
        
        
        
        
        