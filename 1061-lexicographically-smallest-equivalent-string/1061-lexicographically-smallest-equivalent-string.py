class UnionFind:
    def __init__(self,n):
        self.rep={chr(i+97):chr(i+97) for i in range(n)}
        self.size={chr(i+97):i for i in range(n)}
        

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
        
        if self.size[xRep] < self.size[yRep]:
            self.rep[yRep]=xRep
        else:
            self.rep[xRep]=yRep
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        uf=UnionFind(26)
        
        for i in range(len(s1)):
            uf.union(s1[i],s2[i])
            
        result=[]
        
        for base in baseStr:
            parent=uf.find(base)
            result.append(parent)
        return "".join(result)
    
            
            
        