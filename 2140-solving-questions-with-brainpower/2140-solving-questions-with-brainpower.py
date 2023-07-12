class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo={}
        
        
        def dfs(index):
            if index >= len(questions):
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index]=max(dfs(index+1), questions[index][0]+dfs(index+1+questions[index][1]))
            
            
            return memo[index]
        
        
        return dfs(0)
        