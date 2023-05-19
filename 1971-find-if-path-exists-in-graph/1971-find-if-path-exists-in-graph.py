class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph={i:[] for i in range(n)}
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            
        
        
        def bfs(node):
            if node==destination:
                return True
            que=deque([node])
            visited=set([node])
            
            while que:
                curr=que.popleft()
                
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        if neighbor == destination:
                            return True
                        else:
                            que.append(neighbor)
                            visited.add(neighbor)
            
            return False
        
        
        return bfs(source)
    
                        
            
        
        
        
        
        
        
        
        
        
        
        