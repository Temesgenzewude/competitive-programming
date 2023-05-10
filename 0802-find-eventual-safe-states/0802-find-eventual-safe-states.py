class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n=len(graph)
        
        safe_nodes={}
        
        def dfs(node):
            if node in safe_nodes:
                return safe_nodes[node]
            
            safe_nodes[node]=False
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return safe_nodes[neighbor]
            
            safe_nodes[node]=True
            return safe_nodes[node]
        
        
        safe=[]
        
#         for node in range(n):
           
#             if dfs(node):
#                 safe.append(node)
#         return safe
    
                
                
        colors=[0 for _ in range(n)]
        
    
        def topSort(node, colors, graph):
            
            if colors[node]==1:
                return False
            colors[node]=1
            
            for neighbour in graph[node]:
                if colors[neighbour]==2:
                    continue
              
                if not topSort(neighbour, colors, graph):
                    return False
            
           
            colors[node]=2
            return True
        
        safe_states=[]
        
        
        for i in range(n):

            if topSort(i, colors, graph):
                safe_states.append(i)
        
        return safe_states
                    
                    
        
            
            
            
            
            
        