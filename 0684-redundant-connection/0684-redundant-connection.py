class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        
        self.reps={i:i for i in range(1,n+1)}
        self.sizes={i:1 for i in range(1,n+1)}
        
        
        
        def find(x):
            parent=self.reps[x]
            
            while parent != self.reps[parent]:
                parent=self.reps[parent]
                
            while x != self.reps[x]:
                self.reps[x]=parent
                x=self.reps[x]
            
            return parent
        
        def union(x,y):
            xRep=find(x)
            yRep=find(y)
            
            if self.sizes[xRep] > self.sizes[yRep]:
                self.reps[yRep]=xRep
                self.sizes[xRep]+=self.sizes[yRep]
            else:
                self.reps[xRep]=yRep
                self.sizes[yRep]+=self.sizes[xRep]
                
            
        answer=[0,0]
        for u,v in edges:

            if find(u) == find(v):
                answer[0]=u
                answer[1]=v
            union(u,v)
            

        return answer
                
            
        
        
      
        