class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        graph=defaultdict(list)
        
        
        for child, par in edges:
            graph[par].append(child)
            graph[child].append(par)
            
        
        
        def dfs(curr, par):
            
            time=0
            
            for child in graph[curr]:
                
                if child==par:
                    continue
                childTime=dfs(child,curr)
                
                if childTime or hasApple[child]:
                    time+=childTime+2
                
            return time
        
        
        
        return dfs(0,-1)
                
        
        
        
        