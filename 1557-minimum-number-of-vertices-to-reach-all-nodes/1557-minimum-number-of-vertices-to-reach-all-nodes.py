class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    
        indegrees=defaultdict(int)
        for u,v in edges:
            indegrees[v]+=1
        
        result=[]
       
        for vertex in range(n):
            if indegrees[vertex] ==0:
                result.append(vertex)
                
        return result
            
        