class UnionFind:
    def __init__(self,n):
        self.rep=[i for i in range(n)]
        self.size={(i,0):1 for i in range(n)}
        self.mapping={}
        

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
        
        if xRep != yRep:
            self.rep[xRep]=yRep
        # if self.size[xRep] > self.size[yRep]:
        #     self.rep[yRep]=xRep
        #     self.size[xRep]+=self.size[yRep]
        # else:
        #     self.rep[xRep]=yRep
        #     self.size[yRep]+=self.size[xRep]
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        graph=defaultdict(set)
        n=len(accounts)
        
        for i in range(n):
            for j in range(1,len(accounts[i])):
                graph[(i,0)].add(accounts[i][j])
                
        uf = UnionFind(n)
        for idx, value in enumerate(accounts):
            for email in value[1:]:
                if email in uf.mapping:
                    uf.union(uf.mapping[email], idx)
                else:
                    uf.mapping[email]=idx
        
        sets=defaultdict(set)
        
        
        
        for idx in range(n):
            parent=uf.find(idx)
            
            sets[parent] |= set(accounts[idx][1:])
        result=[]
        for key in sets:
            result.append([accounts[key][0]]+sorted(sets[key]))
        return result
            
        
        
                    
        
        # for i in range(n):
        #     for j in range(i, n):
        #         for k in range(1, len(accounts[j])):
        #             if accounts[j][]
                    
                
                
                
                
                
        
        
                
        
        
        
                
                
        