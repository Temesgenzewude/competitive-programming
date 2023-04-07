class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        
        for nod1, nod2 in edges:
            graph[nod1].append(nod2)
            graph[nod2].append(nod1)
       
        
        for node in range(len(graph)):
            if len(graph[node+1])==(len(graph)-1):
                return node+1
        
            
            
            
        