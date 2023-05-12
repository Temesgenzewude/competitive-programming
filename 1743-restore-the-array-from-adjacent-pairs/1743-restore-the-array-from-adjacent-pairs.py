class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph=defaultdict(list)
        
        for adj1, adj2 in adjacentPairs:
            graph[adj1].append(adj2)
            graph[adj2].append(adj1)
        extremes=[]
        
     
            
        for key in graph:
            if len(graph[key])==1:
                extremes.append(key)
                break
                
                    
        
        queue=deque([extremes[0]])
        
        visited=set([extremes[0]])
        result=[extremes[0]]
        
        while queue:
            curr=queue.popleft()
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    result.append(neighbor)
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        
        return result
                
            
            
        
      
                
            
        
        # return [1,2,3,4]
            
        
        
        
        
        
        