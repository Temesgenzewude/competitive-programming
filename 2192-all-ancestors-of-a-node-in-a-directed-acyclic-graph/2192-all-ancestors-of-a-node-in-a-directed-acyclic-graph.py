class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def bfs(edges,n):
            
            indgrees=[0 for _ in range(n)]
            graph=defaultdict(list)
            for source, sink in edges:
                graph[source].append(sink)
                indgrees[sink]+=1

            que=deque()
            
            for i in range(n):
                if indgrees[i]==0:
                    que.append(i)
            
            ancestors=[[] for _ in range(n)]
            
            while que:
                node=que.popleft()
                ancestors[node] = sorted(set(ancestors[node]))
                for neighbor in graph[node]:
                    ancestors[neighbor].append(node)
                    ancestors[neighbor].extend(ancestors[node])
                    indgrees[neighbor]-=1
                    if indgrees[neighbor]==0:
                        que.append(neighbor)
                        
            
            return ancestors
        
        return bfs(edges,n)
        
        
                
                
                
                
                
                
            
            
            
            
            
            
            
            
            
        
        
        return -1
    
            
        