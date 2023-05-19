class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        self.reps={i:i for i in range(n) }
        self.sizes={i:1 for i in range(n)}

        def find(x):
            parent=self.reps[x]

            while parent !=self.reps[parent]:
                parent=self.reps[parent]


            while x !=self.reps[x]:
                self.reps[x]=parent
                x=self.reps[x]


            return parent

        def union(u,v):
            uRep=find(u)
            vRep=find(v)

            if self.sizes[uRep] > self.sizes[vRep]:
                self.reps[vRep]=uRep
                self.sizes[uRep]+=self.sizes[vRep]
            else:
                self.reps[uRep]=vRep
                self.sizes[vRep]+=self.sizes[uRep]

        for u,v in edges:
            union(u,v)
    
        return find(source)==find(destination)
        
        
       
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
        
            
            
    
            
        
    
        