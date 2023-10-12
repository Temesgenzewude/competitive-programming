class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph= defaultdict(list)
        
        for i in range(len(edges)):
            start, end= edges[i]
            prob= succProb[i]
            graph[start].append((end, prob))
            graph[end].append((start, prob))
            
        def dijkstra(graph):
            maxProbs= [0]*n
            maxProbs[start_node]=1
            queue=[(-1, start_node)]
            visited=set()
            
            while queue:
                currProb, currNode= heapq.heappop(queue)
                if currNode in visited:
                    continue
                    
                visited.add(currNode)
                for start, prob in graph[currNode]:
                    newProb= abs(currProb)*prob
                    if newProb > maxProbs[start]:
                        maxProbs[start]=newProb
                        heapq.heappush(queue, (-newProb, start))
            return maxProbs[end_node]
        return dijkstra(graph)
        
        
        
        
                    
        
        
        
        
        
        
        
        
