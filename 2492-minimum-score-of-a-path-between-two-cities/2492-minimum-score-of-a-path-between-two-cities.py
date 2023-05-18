class Solution:
    
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.rep={i:i for i in range(1,n+1)}
        self.size={i:1 for i in range(1,n+1)}
        self.minimum={i: float("inf") for i in range(1,n+1)}
        
        mini_dist=float("inf")
        
        
        for u,v,cost in roads:
            self.union(u,v,cost)
            
        
        return self.minimum[self.find(1)]
    
            
            
            
            
        
    def find(self,node):
        parent=self.rep[node]
        
        while parent != self.rep[parent]:
            parent=self.rep[parent]
        
        while node != self.rep[node]:
            self.rep[node]=parent
            node=self.rep[node]
        return parent
            
    def union(self,x,y,cost):
        xrep=self.find(x)
        yrep=self.find(y)
        
        if self.size[xrep] < self.size[yrep]:
            xrep,yrep=yrep, xrep
        
        self.minimum[xrep]=min(self.minimum[xrep], self.minimum[yrep], cost)
        
        if xrep != yrep:
            self.rep[yrep]=xrep
            self.size[xrep]+=self.size[yrep]
            
    
            
    
    
            
    
    
        
            
            
            
        