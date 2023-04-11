class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph={i:[] for i in range(1, len(isConnected)+1)}
        for i in range(len(isConnected)):
            for idx,ele in enumerate(isConnected[i]):
                if ele == 1 and i !=idx :
                    graph[i+1].append(idx+1)
        
        visited=set()
        provinces=0
        
        def dfs(city):
            nonlocal visited
            for n in graph[city]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)
            
        for city in graph:
            if city not in visited:
                provinces+=1
                visited.add(city)
                dfs(city)
        
        return provinces
                    
                
        