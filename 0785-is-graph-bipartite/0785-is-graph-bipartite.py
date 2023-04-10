class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        groups={}
        
        def bfs(graph):
            colors=[-1]*len(graph)
            
            for i in range(len(graph)):
                if colors[i]==-1:
                    queue=deque()
                    queue.append(i)
                    colors[i]=0
                    
                    while queue:
                        node= queue.popleft()
                        for neighbour in graph[node]:
                            if colors[neighbour]== colors[node]:
                                return False
                            elif colors[neighbour]==-1:
                                queue.append(neighbour)
                                colors[neighbour]=1-colors[node]
            return True
        
        
        return bfs(graph)
                                
    
                
                
            
        
        
        
        
        
                
                
                
                
                
        
        
        
        
        