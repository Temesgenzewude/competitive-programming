class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph=defaultdict(set)
        
        for c1,c2 in roads:
            graph[c1].add(c2)
            graph[c2].add(c1)
            
        
        ans=0
        for c1, c2 in itertools.combinations(graph.keys(),2):
            has_con=1 if c1 in graph[c2] else 0
            
            c1_con=len(graph[c1])
            c2_con=len(graph[c2])
            
            ans=max(ans, c1_con+c2_con-has_con)
            
        
        return ans
            
    
        
        