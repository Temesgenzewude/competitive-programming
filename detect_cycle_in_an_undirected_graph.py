from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    """
	    0->white
	    1->grey
	    2->black
	    """
	    def topSort(graph,colors, node,parent):
	     
	        if node!=parent and colors[node]==1:
	            return True
	        colors[node]=1
	        
	        for neighbor in graph[node]:
	            if neighbor != parent and topSort(graph, colors, neighbor, node):
	                return True
	       
	        colors[node]=2
	        return False
	       
	       
	    colors=[0 for _ in range(V)]
	    
	    parent=-1
	    
	    for node in range(V):
	        if colors[node]==0:
	            if topSort(adj, colors, node,parent):
	                return True
	   
	    return False
