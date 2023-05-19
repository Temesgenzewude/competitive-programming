class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.rep={}
        self.size={}
        
        for u,_,_,v in equations:
            self.rep[u]=u
            self.rep[v]=v
            self.size[u]=1
            self.size[v]=1
            
        for u,ope,_,v in equations:
            if ope == "=":
                self.union(u,v)
        
        for u,ope,_,v in equations:
            if self.find(u)==self.find(v) and ope != "=":
                return False
        return True
    
    
    def find(self,x):
        parent=self.rep[x]
        while parent != self.rep[parent]:
            parent=self.rep[parent]
        
        while x != self.rep[x]:
            self.rep[x]=parent
            x=self.rep[x]
        
        return parent

    def union(self,x,y):
        xRep=self.find(x)
        yRep=self.find(y)
        
        if self.size[xRep] > self.size[yRep]:
            self.rep[yRep]=xRep
            self.size[xRep]+=self.size[yRep]
        else:
            self.rep[xRep]=yRep
            self.size[yRep]+=self.size[xRep]
        
        
        
        
        
        