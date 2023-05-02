class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName=kingName
        self.graph=defaultdict(list)
        self.dead=set()
    
        
        
        

    def birth(self, parentName: str, childName: str) -> None:
        
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        
        
        def dfs(kingName, result):
            if kingName not in self.dead:
                result.append(kingName)
            for child in self.graph[kingName]:
                dfs(child, result)
        
        result=[]
        dfs(self.kingName, result)
        
        return result
       
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()