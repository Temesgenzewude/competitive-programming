class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        if n<3:
            return [node for node in range(n)]
        
        graph=[set() for _ in range(n)]
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves=[]
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)
        
        remainingNodes=n
        while remainingNodes>2:
            remainingNodes-=len(leaves)
            temp=[]
            
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor])==1:
                        temp.append(neighbor)
            leaves=temp
            
        return leaves
    
    
        
        
        
        
        
        
        